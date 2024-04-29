import streamlit as st
import pandas as pd
from datetime import date
from github_contents import GithubContents



st.title("Fragen")

st.text("Bonne Chance, Name")
if "df_fragen" in st.session_state.keys():
    st.dataframe(st.session_state.df_fragen)

# def load_data():
#    return pd.read_csv("Fragen.csv")
# fragen_df = init_dataframe()


# for index, row in fragen_df.iterrows():
#    st.write(row["question"])
#    auswahl = st.radio("answer:", [row["distractor3"], row["distractor1"], row["distractor2"], row["correct_answer"]])
#    if auswahl == row["correct_answer"]:
#        st.success("Richtig! Die Antwort ist " + row["correct_answer"])
#    else:
#        st.error("Falsch! Die richtige Antwort ist " + row["correct_answer"])

st.page_link("pages/page6.py", label="Weiter", icon="😸")
