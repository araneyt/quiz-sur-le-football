import streamlit as st

# Funktion zur Darstellung der Seite "Name eingeben"
def page_enter_name():
    st.title("Namen eingeben")
    name = st.text_input("Bitte geben Sie Ihren Namen ein und bestätigen Sie mit Enter:")
    if name:
        st.session_state.name = name
        st.write(f"Willkommen, {name}!")
        st.write("Klicke unten auf den Link, um das Spiel zu starten.")

# Hauptprogramm
def main():
    # Initialisierung des Namens in der Session, falls nicht vorhanden
    if "name" not in st.session_state:
        st.session_state.name = ""
    page_enter_name()
    # Anzeige des Spiel starten Links, falls ein Name eingegeben wurde
    if st.session_state.name:
        st.page_link("pages/page3.py", label="Hier geht es weiter", icon="🪴")

if __name__ == "__main__":
    main()