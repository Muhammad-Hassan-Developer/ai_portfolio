import streamlit as st

def show_navbar():

    tabs = st.tabs([
        "Home",
        "Services",
        "Projects",
        "Live Demo",
        "About",
        "Contact"
    ])

    return tabs