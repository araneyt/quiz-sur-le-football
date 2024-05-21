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
    # Zufällige Auswahl einer Frage
    random_question = random.choice(questions["question"].values)
    return random_question

# Funktion zur Aktualisierung der Position des Balls basierend auf der Antwort
def update_ball_position(correct):
    if correct:
        st.session_state.ball_position = min(6, st.session_state.ball_position + 1)  # Ball nach rechts bewegen, aber maximal bis zur 6. Markierung
    else:
        st.session_state.ball_position = max(0, st.session_state.ball_position - 1)  # Ball nach links bewegen, aber minimal bis zur 0. Markierung

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

# Funktion zur Überprüfung des Spielstands und Anzeige des entsprechenden GIFs
def check_score():
    if st.session_state.ball_position == 0:
        st.image("Gegentor.gif")
        # Tor-GIF laufen lassen
    elif st.session_state.ball_position == 6:
        st.image("Tor.gif")
        # Tor-GIF laufen lassen

def main():
     # Zugriff auf den eingegebenen Namen von Seite 1
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
    # Initialisierung des Session State, falls noch nicht vorhanden
    if "user_input" not in st.session_state:
        st.session_state.user_input = []
    if "ball_position" not in st.session_state:
        st.session_state.ball_position = 3  # Startposition des Balls in der Mitte
    # Frage anzeigen
    with st.form("answer_form"):
        if 'question_asked' not in st.session_state:
            st.session_state.question_asked = False
        if "question" not in st.session_state:
            st.session_state.question = show_random_question(questions)
        if not st.session_state.question_asked:
            st.write("Frage:", st.session_state.question)
            st.write("Wählen Sie eine oder mehrere Antworten aus:")
            correct_answer = questions.loc[questions["question"] == st.session_state.question, "correct_answer"].values[0]
            distractors = questions.loc[questions["question"] == st.session_state.question, ["distractor1", "distractor2", "distractor3"]].values.flatten().tolist()
            options = distractors + [correct_answer]
            st.session_state.user_input = st.multiselect("Antworten:", options=options, default=st.session_state.user_input)
            submit_button = st.form_submit_button("Antworten überprüfen")
            if submit_button:
                if set(st.session_state.user_input) == set([correct_answer]):
                    st.success("Richtig! Die Antwort(en) ist/sind korrekt.")
                    update_ball_position(correct=True)
                else:
                    st.error("Leider falsch! Die richtige Antwort ist: " + correct_answer)
                    update_ball_position(correct=False)
                show_score()
                check_score()
                st.session_state.question_asked = True

    # Verlinkung zur nächsten Seite mit einem Button
    if st.button("Zur nächsten Frage"):
        st.session_state.question_asked = False
        questions = questions[questions["question"] != st.session_state.question]  # delete the question from the list of questions
        st.session_state.user_input = []
        st.session_state.question = show_random_question(questions) # Reset the question
        st.rerun()

if __name__ == "__main__":
    main()