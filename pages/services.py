import streamlit as st
from components.service_cards import show_services

def show():

    st.title("AI Services")

    show_services()