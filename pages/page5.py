import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

# Laden der Fragen aus der CSV-Datei
@st.cache_resource
def load_questions(filename):
    return pd.read_csv(filename)

# Funktion zur Auswahl und Anzeige einer zufälligen Frage
def show_random_question(questions):
    question_data = questions.sample(1).iloc[0]
    question_text = question_data['question']
    correct_answer = question_data['correct_answer']
    wrong_answers = [question_data[f'distractor{i}'] for i in range(1, 4)]
    
    # Zufällige Position der richtigen Antwort bestimmen
    answers = wrong_answers + [correct_answer]
    random.shuffle(answers)
    
    return question_text, correct_answer, answers

# Funktion zur Aktualisierung der Position des Balls basierend auf der Antwort
def update_ball_position(correct):
    if correct:
        st.session_state.ball_position = max(0, st.session_state.ball_position - 1)  # Ball nach links bewegen, aber minimal bis zur 0. Markierung
    else:
        st.session_state.ball_position = min(6, st.session_state.ball_position + 1)  # Ball nach rechts bewegen, aber maximal bis zur 6. Markierung

# Funktion zur Anzeige des Spielstands
def show_score():
    # Linie mit Markierungen zeichnen
    plt.figure(figsize=(8, 1))
    plt.plot([0, 6], [0, 0], color='black')  # Linie ohne Markierungen
    plt.scatter([1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], marker='|', color='black', s=200)  # Markierungen
    plt.xlim(-0.5, 6.5)
    plt.ylim(-0.5, 0.5)
    plt.axis('off')
    # Ball positionieren
    plt.scatter(st.session_state.ball_position, 0, color='purple', s=200)
    # Diagramm anzeigen
    st.pyplot(plt)

# Funktion zur Überprüfung des Spielstands
def check_score():
    if st.session_state.ball_position == 0:
        st.image("Gegentor.gif")
    elif st.session_state.ball_position == 6:
        st.image("Tor.gif")

# Funktion zum Neustarten des Spiels
def restart_game():
    st.session_state.question_asked = False
    st.session_state.ball_position = 3  # Ballposition zurücksetzen
    st.session_state.user_input = []
    st.session_state.question, st.session_state.correct_answer, st.session_state.answers = show_random_question(load_questions("Fragen.csv"))  # Neue Frage setzen
    st.experimental_rerun()

def main():
    # Initialisierung des Session State, falls noch nicht vorhanden
    if "name" not in st.session_state:
        st.session_state.name = "Spieler"  # Default-Name, falls keiner gesetzt ist
    if "user_input" not in st.session_state:
        st.session_state.user_input = []
    if "ball_position" not in st.session_state:
        st.session_state.ball_position = 3  # Startposition des Balls in der Mitte
    if "question" not in st.session_state:
        st.session_state.question_asked = False
        st.session_state.question, st.session_state.correct_answer, st.session_state.answers = show_random_question(load_questions("Fragen.csv"))

    player_name = st.session_state.name
    # Farbige Box mit dem Titel und dem Namen erstellen
    st.markdown(
        f'<div style="background-color:#c5eef0; padding:10px; border-radius:5px;">'
        f'<h2 style="color:black; font-size:22px;">"On ne fait pas d`omlette sans casser des oeufs" (Man kann kein Omlett machen, ohne Eier zu zerbrechen 🍳):</h2>'
        f'<span style="color:black; font-size:22px;"> {player_name}</span>'
        '</div>',
        unsafe_allow_html=True
    )

    st.title("Quiz zu den Naturwissenschaften")
    # Laden der Fragen aus der CSV-Datei
    questions = load_questions("Fragen.csv")

    # Frage anzeigen
    with st.form("answer_form"):
        if not st.session_state.question_asked:
            st.write("Frage:", st.session_state.question)
            st.write("Wählen Sie eine oder mehrere Antworten aus:")
            st.session_state.user_input = st.multiselect("Antworten:", options=st.session_state.answers, default=st.session_state.user_input)
            submit_button = st.form_submit_button("Antworten überprüfen")
            if submit_button:
                if set(st.session_state.user_input) == set([st.session_state.correct_answer]):
                    st.success("Richtig! Die Antwort(en) ist/sind korrekt.")
                    update_ball_position(correct=True)
                else:
                    st.error("Leider falsch! Die richtige Antwort ist: " + st.session_state.correct_answer)
                    update_ball_position(correct=False)
                show_score()
                st.session_state.question_asked = True

    # Anzeige der GIFs bei Tor und Neustart-Button
    if st.session_state.ball_position == 0:
        st.image("Tor.gif")
        if st.button("Spiel Neustarten"):
            restart_game()
    elif st.session_state.ball_position == 6:
        st.image("Gegentor.gif")
        if st.button("Spiel Neustarten"):
            restart_game()
    else:
        # Verlinkung zur nächsten Frage mit einem Button, wenn kein Tor geschossen wurde
        if st.session_state.question_asked and st.button("Zur nächsten Frage"):
            st.session_state.question_asked = False
            questions = questions[questions["question"] != st.session_state.question]  # Frage aus der Liste der Fragen entfernen
            st.session_state.user_input = []
            st.session_state.question, st.session_state.correct_answer, st.session_state.answers = show_random_question(questions)  # Neue Frage setzen
            st.experimental_rerun()

if __name__ == "__main__":
    main()
