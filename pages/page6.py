import streamlit as st
import pandas as pd
import random

# Laden der Fragen aus der CSV-Datei
@st.cache_resource
def load_questions(filename):
    return pd.read_csv(filename)

def main():
    st.title("Tischfußballspiel")

    st.write("Willkommen zum Tischfußballspiel! Beantworte die Fragen richtig, um Tore zu erzielen.")

    # Initialisierung des Session States
    if "ball_position" not in st.session_state:
        st.session_state.ball_position = 3 # Der Ball startet in der Mitte
        st.session_state.left_score = 0
        st.session_state.right_score = 0

    # Laden der Fragen aus der CSV-Datei
    questions = load_questions("Fragen.csv")

    # Zufällige Auswahl einer Frage
    random_question = random.choice(questions["question"].values)
    correct_answer = questions.loc[questions["question"] == random_question, "correct_answer"].values[0]
    distractors = [questions.loc[questions["question"] == random_question, f"distractor{i}"].values[0] for i in range(1, 4)]
    options = distractors + [correct_answer]

    # Frage anzeigen und Antwort des Nutzers erfassen
    user_answer = st.radio(random_question, options)

    # Antwort überprüfen und Ball bewegen
    if user_answer == correct_answer:
        st.session_state.ball_position += 1
        st.write("Richtig! Tor für dich!")
    else:
        st.session_state.ball_position -= 1
        st.write("Falsch! Gegentor!")

    # Ballposition überprüfen und Tor zählen
    if st.session_state.ball_position == 0:
        st.session_state.right_score += 1
        st.write("Tor für rechts!")
    elif st.session_state.ball_position == 6:
        st.session_state.left_score += 1
        st.write("Tor für links!")

    # Spielstand aktualisieren
    st.write(f"Spielstand: Links {st.session_state.left_score} - {st.session_state.right_score} Rechts")

    # Spielende anzeigen
    if st.session_state.left_score < 3 and st.session_state.right_score < 3:
        st.write("Nächste Frage...")
    else:
        st.write("Spiel vorbei!")
        if st.session_state.left_score > st.session_state.right_score:
            st.write("Links gewinnt!")
        else:
            st.write("Rechts gewinnt!")

if __name__ == "__main__":
    main()
