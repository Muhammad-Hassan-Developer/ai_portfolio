import streamlit as st

def rag_projects():

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="project-card">
        <h3>Medical RAG</h3>
        Chat with medical documents
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card">
        <h3>Research Paper RAG</h3>
        Research assistant chatbot
        </div>
        """, unsafe_allow_html=True)