import streamlit as st
from voice_recognize import vosk_voice_recignize

def voice_recignizing_button(model):
    st.markdown(
         """
        <style>
        .stButton{
            position: fixed;
            right: 20px;
            bottom: 20px; 
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    if st.button("",key='voice_button'):
      try:
       text = vosk_voice_recignize(model)
       st.write(f"Вы сказали: {text}")
      except sr.UnknownValueError:
            st.write("Кажется, не удалось распознать речь")
      except sr.RequestError:
                st.write("Кажется, возникла проблема с доступом к сервисам распознавания речи")
