import streamlit as st
import ollama
desiredModel = "llama3.2:latest"

st.title("LLM Web App")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Reset Conversation"):
    st.session_state.messages = []
    st.rerun()    


def generate_response(Question):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": Question,
        }
    )

    response = ollama.chat(
        model=desiredModel,
        messages=st.session_state.messages,
    )

    reply = response["message"]["content"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply,
        }
    )

    st.info(reply)

with st.form("MyForm"):
    text = st.text_area(
        "Enter text:",
        "Ask a question and press the submit button",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)