import streamlit as st
from src.model import model_options

def sidebar():
    with st.sidebar:
        st.header("Model Settings")
        st.sidebar.selectbox("Select a model", list(model_options.keys()), key="model_name")
        with st.expander("More settings"):
            st.slider(
                "Temperature", min_value=0.0, max_value=2.0, step=0.1, value=0.1, key="temperature"
            )
            st.slider(
                "Max Tokens", min_value=0, max_value=8000, value=1000, key="max_tokens"
            )