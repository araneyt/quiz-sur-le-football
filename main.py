import streamlit as st
import pandas as pd
from datetime import date
from github_contents import GithubContents

# Set page configuration
st.set_page_config(page_title="Quiz sur le football", page_icon="⚽", layout="wide",  
                   initial_sidebar_state="expanded")
st.title("Bienvenue au quiz sur le football")


def frage_und_antwort(frage, antworten, richtige_antwort):
   st.write(frage)
   auswahl = st.radio("Antworten:", antworten)
   if auswahl == richtige_antwort:
       st.success("Richtig! Die Antwort ist " + richtige_antwort)
   else:
       st.error("Falsch! Die richtige Antwort ist " + richtige_antwort)
def main():
   st.title("Wissenstest")
   # Lese die Fragen aus der CSV-Datei ein
   fragen_df = pd.read_csv("fragen.csv")
   # Iteriere über die Zeilen der DataFrame
   for index, row in fragen_df.iterrows():
       frage_und_antwort(row['Frage'],
                         [row['Antwort_1'], row['Antwort_2'], row['Antwort_3'], row['Antwort_4']],
                         row['Richtige_Antwort'])
if __name__ == "__main__":
   main()
