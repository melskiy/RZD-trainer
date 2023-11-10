import streamlit as st
from voice_recignizing_button import voice_recignizing_button
from jsrecordbutton import jsbutton
import vosk
def main():
    model = vosk.Model("vosk-model-small-ru-0.22")
    st.title("Голосовой ассистент")

    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    jsbutton()

if __name__ == "__main__":
    main()