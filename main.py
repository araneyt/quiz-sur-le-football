import streamlit as st
import pandas as pd
from datetime import date
from github_contents import GithubContents

DATA_FILE = "Fragen.csv"


def init_github():
    """Initialize the GithubContents object."""
    if 'github' not in st.session_state:
        st.session_state.github = GithubContents(
            st.secrets["github"]["owner"],
            st.secrets["github"]["repo"],
            st.secrets["github"]["token"])

def init_dataframe():
    """Initialize or load the dataframe."""
    if 'df_fragen' in st.session_state:
        pass
    else:
        st.session_state.df_fragen = st.session_state.github.read_df(DATA_FILE)

    st.set_page_config(
        page_title="Quiz sur le football",
        page_icon="⚽",
    )

def main():  
    init_github()
    init_dataframe()
    st.title("Bienvenue au quiz sur le football  ⚽")

    st.image('Fussballspieler.jpg')

    st.page_link("page1.py", label="Drücke um zu starten", icon="😸")

if __name__ == "__main__":
    main()
