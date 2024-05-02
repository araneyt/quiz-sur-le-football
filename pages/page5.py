import streamlit as st
import pandas as pd
import random

# Laden der Fragen aus der CSV-Datei
@st.cache
def load_questions(filename):
    return pd.read_csv(filename)

# Funktion zur Auswahl und Anzeige einer zufälligen Frage
def show_random_question(questions):
    # Zufällige Auswahl einer Frage
    random_question = random.choice(questions["question"].values)
    return random_question

# Hauptprogramm
def main():
    st.title("Quiz zu den Naturwissenschaften")

    # Laden der Fragen aus der CSV-Datei
    questions = load_questions("Fragen.csv")

    # Frage anzeigen
    question = show_random_question(questions)
    st.write("Frage:", question)

    # Anzeigen der Antwortmöglichkeiten
    st.write("Wählen Sie eine Antwort aus:")
    correct_answer = questions.loc[questions["question"] == question, "correct_answer"].values[0]
    distractors = questions.loc[questions["question"] == question, ["distractor1", "distractor2", "distractor3"]].values.flatten().tolist()
    answers = distractors + [correct_answer]
    random.shuffle(answers)
    selected_answer = st.radio("Antworten:", options=answers)

    # Überprüfung der Antwort und Anzeige der richtigen Antwort
    if selected_answer:
        if selected_answer == correct_answer:
            st.success("Richtig! Die Antwort ist: " + selected_answer)
        else:
            st.error("Leider falsch! Die richtige Antwort ist: " + correct_answer)

if __name__ == "__main__":
    main()
