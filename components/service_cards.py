import streamlit as st

def show_services():

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="service-card">
        <h3>RAG Systems</h3>
        Knowledge based AI chatbots.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="service-card">
        <h3>LLM Applications</h3>
        Summarization and translation tools.
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="service-card">
        <h3>ML Prediction</h3>
        Machine learning prediction systems.
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="service-card">
        <h3>Voice AI</h3>
        Speech recognition assistants.
        </div>
        """, unsafe_allow_html=True)