import streamlit as st
import pandas as pd
import random
import time

# Laden der Fragen aus der CSV-Datei
@st.cache
def load_questions(filename):
    return pd.read_csv(filename)

# Funktion zur Anzeige einer zufälligen Frage
def show_question_and_answers(questions):
    # Zufällige Auswahl einer Frage
    random_question = random.choice(questions["question"].values)
    st.write("Frage:", random_question)

    # Anzeige der Antwortmöglichkeiten
    answers = questions.loc[questions["question"] == random_question, ["distractor1", "distractor2", "distractor3", "correct_answer"]].values[0]
    st.write("Antwortmöglichkeiten:")
    for answer in answers:
        st.write("-", answer)

    return random_question

# Hauptprogramm
def main():
    st.title("Quiz zu den Naturwissenschaften")

    # Laden der Fragen aus der CSV-Datei
    questions = load_questions("Fragen.csv")

    # Anzeige einer zufälligen Frage und Antwortmöglichkeiten
    question = show_question_and_answers(questions)

    # Timer von 10 herunterzählen (Zeit zum Lesen der Frage und Auswahl der Antwort)
    st.write("Sie haben 15 Sekunden Zeit, um eine Antwort auszuwählen.")
    for i in range(15, 0, -1):
        st.write(f"Verbleibende Zeit: {i} Sekunden")
        time.sleep(1)

    # Überprüfung, ob die Antwort korrekt ist
    selected_answer = st.text_input("Geben Sie Ihre Antwort ein:")
    correct_answer = questions.loc[questions["question"] == question, "correct_answer"].values[0]
    if selected_answer == correct_answer:
        st.success("Richtig! Die Antwort ist: " + selected_answer)
    else:
        st.error("Falsch! Die richtige Antwort ist: " + correct_answer)
if __name__ == "__main__":
    main()




