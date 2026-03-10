import streamlit as st
from api_clients.rag_api import ask_rag

def rag_chat():

    st.markdown('<div class="chat-box">', unsafe_allow_html=True)

    st.subheader("RAG Chat Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.chat_input("Ask something from knowledge base")

    if user_input:

        st.session_state.messages.append(
            {"role":"user","content":user_input}
        )

        answer = ask_rag(user_input)

        st.session_state.messages.append(
            {"role":"assistant","content":answer}
        )

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    st.markdown('</div>', unsafe_allow_html=True)