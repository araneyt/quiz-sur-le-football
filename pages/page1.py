import streamlit as st

title = st.text_input('Gib deinen Namen ein', 'Elena')
st.write('Spielername', title)

st.page_link("pages/page2.py", label="Weiter", icon="😸")
