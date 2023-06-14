import streamlit as st
from pathlib import Path

parent_path = Path(__file__).parent.parent

def front_page():
    # st.header("Page Front Content")
    # Graphic
    # title
    # intro
    show_initial_text()

def show_initial_text():
    st.subheader("Questionnaire Overview")
    st.markdown("""
        This **interactive web interface** offers a quick and engaging way to assess your psychopatic, narcistic, and Machiavellian tendencies. No lengthy explanations or excessive reading required!
        Simply answer 28 questions by selecting a score from 1(disagree) to 5 (agree). It's as easy as giving your honest opinion.
    """)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    # Display an image from a file
    image_file = Path(parent_path, "images", "chess (1).jpg").absolute().as_posix()
    st.image(image_file, use_column_width=True)
