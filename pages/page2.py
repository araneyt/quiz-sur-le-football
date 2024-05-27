import streamlit as st

def main():
    # Zugriff auf den eingegebenen Namen von Seite 1
    player_name = st.session_state.name
    # Farbige Box mit dem Titel und dem Namen erstellen
    st.markdown(
        f'<div style="background-color:#c5eef0; padding:10px; border-radius:5px;">'
        f'<h2 style="color:black; font-size:22px;">C`est en forgeant qu`on devient forgeron (Übung macht den Meister):</h2>'
        f'<span style="color:black; font-size:22px;"> {player_name}</span>'
        '</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

st.title("Wähle deinen Schwierigkeitsgrad aus")
# Regler für Schwierigkeitsgrad
color = st.select_slider(
    'Du kannst zwischen Einfach, Mittel und Schwierig auswählen',
options=['Einfach', 'Mittel', 'Schwierig'])
st.write('Dein Schwierigkeitsgrad ist', color)
#Einfügen Hilfetext 
st.write('❕ Wenn Du dich traust, ist unterhalb des Bildes ein Button, um zum Spiel zu gelangen')
#Bild einer schreinenden Frau einfügen
st.image("Bilder/Frau.jpg") 
#Verlinkung zur nächsten Seite mit einem Button
st.page_link("pages/page3.py", label="Spiel beginnen", icon="🪴")
