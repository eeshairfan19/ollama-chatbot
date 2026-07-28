import streamlit as st
import ollama
desiredModel = "llama3.2:latest"

st.title("LLM Web App")

def generate_response(Question):
    response = ollama.chat(model= desiredModel, messages =[
        {
            "role": "user",
            "content" : Question,
        },
    ])
    st.info(response["message"]["content"])

with st.form("MyForm"):
    text = st.text_area(
        "Enter text:",
        "Ask a question and press the submit button",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)