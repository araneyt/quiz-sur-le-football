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

# Hauptprogramm
def main():
    st.title("Quiz zu den Naturwissenschaften")

    # Laden der Fragen aus der CSV-Datei
    questions = load_questions("Fragen.csv")

    # Anzeige einer zufälligen Frage
    question = show_question(questions)

    # Timer von 10 herunterzählen (Zeit zum Lesen der Frage)
    st.write("Bitte lesen Sie die Frage sorgfältig.")
    for i in range(10, 0, -1):
        st.write(f"Timer zum Lesen der Frage: {i} Sekunden")
        time.sleep(1)

    # Anzeige der Antwortmöglichkeiten
    st.write("Bitte wählen Sie eine Antwort aus.")
    selected_answer = st.radio("Antworten:", options=["A", "B", "C", "D"])

    # Timer von 15 herunterzählen (Zeit zum Auswählen der Antwort)
    st.write("Die Zeit zum Auswählen der Antwort beginnt jetzt.")
    for i in range(15, 0, -1):
        st.write(f"Timer zum Auswählen der Antwort: {i} Sekunden")
        time.sleep(1)

    # Überprüfung, ob die Antwort korrekt ist
    correct_answer = questions.loc[questions["question"] == question, "correct_answer"].values[0]
    if selected_answer == correct_answer:
        st.success("Richtig! Die Antwort ist: " + selected_answer)
    else:
        st.error("Falsch! Die richtige Antwort ist: " + correct_answer)

if __name__ == "__main__":
    main()




