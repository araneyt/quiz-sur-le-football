import streamlit as st
import pandas as pd
import random
import streamlit as st
 
 
# Laden der Fragen aus der CSV-Datei
@st.cache_resource
def load_questions(filename):
    return pd.read_csv(filename)
 
# Funktion zur Auswahl und Anzeige einer zufälligen Frage
def show_random_question(questions):
    # Zufällige Auswahl einer Frage
    random_question = random.choice(questions["question"].values)
    return random_question
 
 
def main():
    st.title("Quiz zu den Naturwissenschaften")
    # Laden der Fragen aus der CSV-Datei
    questions = load_questions("Fragen.csv")
    # Initialisierung des Session State, falls noch nicht vorhanden
    if "user_input" not in st.session_state:
        st.session_state.user_input = []
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
            submit_button=st.form_submit_button("Antworten überprüfen")
            if submit_button:
                if set(st.session_state.user_input) == set([correct_answer]):
                    st.success("Richtig! Die Antwort(en) ist/sind korrekt.")
                else:
                    st.error("Leider falsch! Die richtige Antwort ist: " + correct_answer)
                st.session_state.question_asked = True
                
 
    # Button zur neuen Frage
    if st.button("Zur nächsten Frage"):
        st.session_state.question_asked = False
        questions = questions[questions["question"] != st.session_state.question]  # delete the question from the list of questions
        st.session_state.user_input = []
        st.session_state.question = show_random_question(questions) # Reset the question
        st.rerun()
 
 
if __name__ == "__main__":
    main()
 