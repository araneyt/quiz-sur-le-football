import streamlit as st
import pandas as pd
from datetime import date
from github_contents import GithubContents


def init_github():
    """Initialize the GithubContents object."""
    if 'github' not in st.session_state:
        st.session_state.github = GithubContents(
            st.secrets["github"]["owner"],
            st.secrets["github"]["repo"],
            st.secrets["github"]["token"])
import streamlit as st


st.set_page_config(
    page_title="Quiz sur le football",
    page_icon="⚽",
)

st.title("Bienvenue au quiz sur le football  ⚽")

st.sidebar.success("Wie ist dein Name?")

st.image('Fussballspieler.jpg')

st.page_link("main.py", label="Startseite", icon="🏠")
st.page_link("page1.py", label="Seite 1", icon="1️⃣")
