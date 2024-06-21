import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

model_options = {
    "GPT-3.5 Turbo-16k": "gpt-3.5-turbo-16k",
    "GPT-4o": "gpt-4o",
    "GPT-4 Turbo": "gpt-4-1106-preview",
    "GPT-4": "gpt-4",
}

llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate(prompt):
    response = llm.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model_options[st.session_state.model_name] if "model_name" in st.session_state else "gpt-3.5-turbo-16k",
        temperature=st.session_state.temperature if "temperature" in st.session_state else 1,
        max_tokens=st.session_state.max_tokens if "max_tokens" in st.session_state else 1000,
    )
    return response.choices[0].message.content



