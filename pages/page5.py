import streamlit as st
import pandas as pd
import random
from streamlit import session_state
 
# Laden der Fragen aus der CSV-Datei
@st.cache_resource
def load_questions(filename):
    return pd.read_csv(filename)
 
# Funktion zur Auswahl und Anzeige einer zufälligen Frage
def show_random_question(questions):
    # Zufällige Auswahl einer Frage
    random_question = random.choice(questions["question"].values)
    return random_question
 
# Hauptprogramm
import streamlit as st
 
def main():
    st.title("Quiz zu den Naturwissenschaften")
    # Laden der Fragen aus der CSV-Datei
    questions = load_questions("Fragen.csv")
    # Initialisierung des Session State, falls noch nicht vorhanden
    if "user_input" not in st.session_state:
        st.session_state.user_input = []
    # Frage anzeigen
    
    with st.form("answer_form"):
        st.session_state.question = show_random_question(questions)
        question = st.session_state.question
        st.write("Frage:", question)
        # Anzeigen der Antwortmöglichkeiten als Multiselect
        st.write("Wählen Sie eine oder mehrere Antworten aus:")
        correct_answer = questions.loc[questions["question"] == question, "correct_answer"].values[0]
        distractors = questions.loc[questions["question"] == question, ["distractor1", "distractor2", "distractor3"]].values.flatten().tolist()
        options = distractors + [correct_answer]
        # Use st.form to prevent reloading until submit
        selected_answers = st.multiselect("Antworten:", options=options, default=st.session_state.user_input)
        submit_button=st.form_submit_button("Antworten überprüfen")
        if submit_button: 
            # Benutzereingaben im Session State speichern
            st.session_state.user_input = selected_answers
    # Überprüfung der Antworten und Anzeige der richtigen Antwort
            if selected_answers:
                if set(selected_answers) == set([correct_answer]):
                    st.success("Richtig! Die Antwort(en) ist/sind korrekt.")
                else:
                    st.error("Leider falsch! Die richtige Antwort ist: " + correct_answer)



    # Button zur nächsten Seite
    if st.button("Zur nächsten Frage"):
        pass  # Add your logic here for the next question
 
if __name__ == "__main__":
    main()
 

