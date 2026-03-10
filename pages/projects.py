import streamlit as st
from components.project_cards import rag_projects

def show():

    st.title("Projects")

    tabs = st.tabs([
        "RAG Systems",
        "LLM Applications",
        "ML Models",
        "Voice AI"
    ])

    with tabs[0]:
        rag_projects()

    with tabs[1]:
        st.info("LLM apps coming soon")

    with tabs[2]:
        st.info("ML projects coming soon")

    with tabs[3]:
        st.info("Voice AI coming soon")