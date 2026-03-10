import streamlit as st
from pathlib import Path

from components.navbar import show_navbar

st.set_page_config(
    page_title="AI Portfolio",
    layout="wide"
)

# Load CSS
css = Path("styles/style.css").read_text()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Navbar Tabs
tabs = show_navbar()

# Import Pages
from pages import home, services, projects, demos, about, contact

with tabs[0]:
    home.show()

with tabs[1]:
    services.show()

with tabs[2]:
    projects.show()

with tabs[3]:
    demos.show()

with tabs[4]:
    about.show()

with tabs[5]:
    contact.show()