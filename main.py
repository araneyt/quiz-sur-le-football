import streamlit as st
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

def main():
    st.set_page_config(
        page_title="Quiz sur le football",
        page_icon="⚽",
        layout="centered",  # Zentriert den Hauptinhalt
        initial_sidebar_state="collapsed"  # Seitenleiste zuklappen
    )

    # CSS um den Abstand zu definieren
    st.markdown(
        """
        <style>
        .stApp {
            max-width: 1200px; /* Maximale Breite des Inhaltsbereichs */
            margin: 0 auto; /* Zentriert den Inhaltsbereich */
            padding: 0 20px; /* Fester Abstand auf beiden Seiten */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialisiere die GitHub-Verbindung
    init_github()

    # Lade oder initialisiere das DataFrame
    init_dataframe()

    st.title("Bienvenue au quiz sur le football  ⚽")
    st.image('Fussballspieler.jpg')
    st.page_link("pages/page1.py", label="Drücke hier um dein Wissen über Naturwissenschaften zu testen", icon="🪴")

if __name__ == "__main__":
    main()
