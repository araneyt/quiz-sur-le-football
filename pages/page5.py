import streamlit as st
import pandas as pd
import random
import time

# Laden der Fragen aus der CSV-Datei
@st.cache
def load_questions(filename):
    return pd.read_csv(filename)

# Funktion zur Anzeige einer zufälligen Frage und Antwortmöglichkeiten
def show_question_and_answers(questions):
    # Zufällige Auswahl einer Frage
    random_question = random.choice(questions["question"].values)
    st.write("Frage:", random_question)

    # Zufällige Auswahl der Antwortmöglichkeiten
    distractors = list(questions.loc[questions["question"] == random_question, ["distractor1", "distractor2", "distractor3"]].values[0])
    correct_answer = questions.loc[questions["question"] == random_question, "correct_answer"].values[0]

    # Überprüfen, ob die richtige Antwort bereits in den Ablenkern enthalten ist
    if correct_answer not in distractors:
        distractors.append(correct_answer)

    # Antworten mischen
    random.shuffle(distractors)

    # Anzeige der Antwortmöglichkeiten als Auswahlmöglichkeiten
    selected_answer = st.selectbox("Antwortmöglichkeiten:", options=distractors)

    return random_question, selected_answer, correct_answer

# Hauptprogramm
def main():
    st.title("Quiz zu den Naturwissenschaften")

    # Laden der Fragen aus der CSV-Datei
    questions = load_questions("Fragen.csv")

    # Anzeige einer zufälligen Frage und Antwortmöglichkeiten
    st.write("Bitte lesen Sie die Frage und wählen Sie dann eine Antwort aus.")
    st.write("Sie haben 10 Sekunden Zeit, um die Frage zu lesen.")
    question, selected_answer, correct_answer = show_question_and_answers(questions)

    # Timer von 10 herunterzählen (Zeit zum Lesen der Frage)
    remaining_time = 10
    while remaining_time > 0:
        st.write(f"Verbleibende Zeit zum Lesen der Frage: {remaining_time} Sekunden")
        time.sleep(1)
        remaining_time -= 1

    # Timer von 15 herunterzählen (Zeit zum Auswählen der Antwort)
    st.write("Sie haben 15 Sekunden Zeit, um eine Antwort auszuwählen.")
    remaining_time = 15
    while remaining_time > 0:
        st.write(f"Verbleibende Zeit zum Auswählen der Antwort: {remaining_time} Sekunden")
        time.sleep(1)
        remaining_time -= 1

    # Überprüfung, ob die Antwort korrekt ist
    if selected_answer == correct_answer:
        st.success("Richtig! Die Antwort ist: " + correct_answer)
    else:
        st.error("Falsch! Die richtige Antwort ist: " + correct_answer)

if __name__ == "__main__":
    main()

