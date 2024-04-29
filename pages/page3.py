import streamlit as st

st.title("Wähle deinen Schwierigkeitsgrad aus")

color = st.select_slider(
    'Du kannst zwischen Einfach, Mittel und Schwierig auswählen',
options=['Einfach', 'Mittel', 'Schwierig'])
st.write('Dein Schwierigkeitsgrad ist', color)

st.image('Frau.jpg')

st.page_link("pages/page4.py", label="Weiter", icon="😸")