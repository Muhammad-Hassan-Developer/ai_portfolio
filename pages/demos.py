import streamlit as st
from components.rag_chat import rag_chat

def show():

    st.title("Live AI Demos")

    tabs = st.tabs([
        "RAG Chat",
        "Summarization",
        "Translation",
        "ML Prediction"
    ])

    with tabs[0]:
        rag_chat()

    with tabs[1]:
        st.subheader("Text Summarization")

        text = st.text_area(
            "Enter text",
            key="summary_text"
        )

        if st.button("Summarize", key="summary_btn"):
            st.write("Summary will appear here")

    with tabs[2]:
        st.subheader("Translation")

        text = st.text_area(
            "Enter text",
            key="translate_text"
        )

        if st.button("Translate", key="translate_btn"):
            st.write("Translation will appear here")

    with tabs[3]:
        st.subheader("ML Prediction")

        age = st.number_input(
            "Age",
            key="age_input"
        )

        chol = st.number_input(
            "Cholesterol",
            key="chol_input"
        )

        if st.button("Predict", key="predict_btn"):
            st.write("Prediction result")