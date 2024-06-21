import streamlit as st
from src.model import generate
from src.prompt import recipe_prompt_template
from src.ui import sidebar

if "messages" not in st.session_state:
    st.session_state.messages = []

def display_chat():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("Enter the ingredients you have..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        prompt = recipe_prompt_template(user_input) # Prompt based on the user input
        response = generate(prompt) # Generates a response based on the prompt

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

def main():
    st.set_page_config(page_title="Recipe Builder", page_icon="🍽️")
    st.title(':gray[Recipe Builder] 🍽️')
    sidebar()
    display_chat()

if __name__ == "__main__":
    main()