import streamlit as st
import time

def main():
    # Zugriff auf den eingegebenen Namen von Seite 1
    player_name = st.session_state.name
    # Farbige Box mit dem Titel und dem Namen erstellen
    st.markdown(
        f'<div style="background-color:#c5eef0; padding:10px; border-radius:5px;">'
        f'<h2 style="color:black; font-size:22px;">"Après la pluie, le beau temps." (Nach dem Regen kommt Sonnenschein 🌞):</h2>'
        f'<span style="color:black; font-size:22px;"> {player_name}</span>'
        '</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

def main():
    st.title("Mach dich bereit!")

    # Timer von 10 herunterzählen
    timer_text = st.empty()
    for i in range(5, 0, -1):
        timer_text.text(f"Timer: {i}")
        time.sleep(1)

    # Ausblenden des Bildes im Hintergrund
    st.markdown('<style>body {background-image: none}</style>', unsafe_allow_html=True)
    #Verlinkung zur nächsten Seite mit einem Button
    st.page_link("pages/page5.py", label="Los geht's", icon="🪴")

if __name__ == "__main__":
    main()

