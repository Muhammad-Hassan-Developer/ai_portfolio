import streamlit as st


st.set_page_config(
    page_title="AI Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"  # <---- hide sidebar
)
def show():

    st.title("About")

    st.write(
    """
    AI Engineer specializing in:

    • RAG systems  
    • LangChain applications  
    • AI APIs  
    • Machine learning models
    """
    )