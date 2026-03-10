import streamlit as st
from components.service_cards import show_services

def show():

    st.markdown(
    """
    <div class="hero">
        <h1>Muhammad Hassan</h1>
        <h3>AI Engineer | RAG Systems | LLM Applications</h3>
        <p>I build AI assistants, RAG systems, and ML prediction APIs.</p>
    </div>
    """,
    unsafe_allow_html=True
    )

    st.header("Services")

    show_services()