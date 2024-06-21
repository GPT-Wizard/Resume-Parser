import streamlit as st
from pypdf import PdfReader
from src.model import model_options

def sidebar():
    with st.sidebar:
        st.title("Building a Generative AI Application: Resume Parser 📝🤖")
        st.info(
            "We will build a Generative AI application using a Large Language Model (LLM) to parse resumes."
        )
        st.markdown("---")
        st.header("Model Settings")
        st.sidebar.selectbox("Select a model", list(model_options.keys()), key="model_name")
        with st.expander("More settings"):
            st.slider(
                "Temperature", min_value=0.0, max_value=2.0, step=0.1, value=0.1, key="temperature"
            )
            st.slider(
                "Max Tokens", min_value=0, max_value=8000, value=1000, key="max_tokens"
            )
        st.markdown("---")
        st.image("src/assets/gpt-wizard.png")
        st.image("src/assets/tw-logo.png")

def file_uploader():
    uploaded_file = st.file_uploader("Upload Candidate Resume PDF", type="pdf")
    if uploaded_file:
        resume_text = ""
        reader = PdfReader(uploaded_file)
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            resume_text += page.extract_text()
        return resume_text