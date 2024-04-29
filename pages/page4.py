import streamlit as st
import time

def main():
    st.title("Start")

    # Timer von 10 herunterzählen
    timer_text = st.empty()
    for i in range(10, 0, -1):
        timer_text.text(f"Timer: {i}")
        time.sleep(1)

st.page_link("pages/page5.py", label="Weiter", icon="😸")

if __name__ == "__main__":
    main()
