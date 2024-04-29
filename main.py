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
    # Setze die Streamlit-Seitenkonfiguration als erste Anweisung
    st.set_page_config(
        page_title="Quiz sur le football",
        page_icon="⚽",
    )

    # Initialisiere die GitHub-Verbindung
    init_github()

    # Lade oder initialisiere das DataFrame
    init_dataframe()

    # Rest deines Codes...
    st.title("Bienvenue au quiz sur le football  ⚽")
    st.image('Fussballspieler.jpg')
    st.page_link("pages/page1.py", label="Drücke um zu starten", icon="😸")

if __name__ == "__main__":
    main()
