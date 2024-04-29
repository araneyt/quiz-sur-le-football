import streamlit as st
import pandas as pd
import random
import time
 
# Laden der Fragen aus der CSV-Datei
@st.cache
def load_questions(filename):
    return pd.read_csv(filename)
# Funktion zur Anzeige einer zufälligen Frage
def show_question(questions):
    # Zufällige Auswahl einer Frage
    random_question = random.choice(questions["question"].values)
    st.write("Frage:", random_question)
    return random_question
 
# Funktion zur Anzeige der Antwortmöglichkeiten
def show_answers(questions, correct_answer):
    # Zufällige Auswahl von 4 Antworten (einschließlich der richtigen Antwort)
    answers = [correct_answer]
    while len(answers) < 4:
        random_answer = random.choice(questions[["distractor1", "distractor2", "distractor3", "correct_answer"]].values.flatten())
        if random_answer not in answers:
            answers.append(random_answer)
 
    random.shuffle(answers)
 
    # Anzeigen der Antworten und Auswahl durch den Benutzer
    selected_answer = st.radio("Antworten:", options=answers, index=None)
    return selected_answer
 
# Hauptprogramm
def main():
    st.title("Quiz zu den Naturwissenschaften")
 
    # Laden der Fragen aus der CSV-Datei
    questions = load_questions("Fragen.csv")
 
    # Anzeige einer zufälligen Frage
    question = show_question(questions)
 
    # Timer von 10 herunterzählen
    timer_text = st.empty()
    for i in range(10, 0, -1):
        timer_text.text(f"Timer: {i}")
        time.sleep(1)
 
    # Anzeige der Antwortmöglichkeiten
    correct_answer = questions.loc[questions["question"] == question, "distractor1"].values[0]
    selected_answer = show_answers(questions, correct_answer)
 
    # Überprüfung, ob die Antwort korrekt ist
    if selected_answer == correct_answer:
        st.success("Richtig! Die Antwort ist: " + selected_answer)
    else:
        st.error("Falsch! Die richtige Antwort ist: " + correct_answer)
 
if __name__ == "__main__":
    main()
