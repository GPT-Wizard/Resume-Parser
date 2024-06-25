import streamlit as st
from src.model import generate
from src.prompt import basic_prompt_template, summary_prompt_template
from src.ui import sidebar, file_uploader

if "messages" not in st.session_state:
    st.session_state.messages = []

job_description = """
Job Title: Senior Software Engineer - Data Processing and API Integration
Company: TechWave Solutions
Job Description:
TechWave Solutions is seeking a Senior Software Engineer with expertise in data processing, API integration, and system architecture. The ideal candidate will lead the development and optimization of scalable data processing systems, collaborate with cross-functional teams, and implement robust software solutions. Key responsibilities include designing custom APIs, enhancing system performance, and participating in on-call rotations for critical production support.
Requirements:
The candidate should have a Bachelor's degree in Computer Science or a related field, with 5+ years of experience in software development. Proficiency in Python, Java, SQL, and AWS services is essential. Strong problem-solving skills, effective communication, and experience in leading technical projects are crucial. Familiarity with front-end technologies like React and Node.js is a plus, as is experience in the fintech or payments industry.
"""


def display_chat(resume):
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("Enter the ingredients you have..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        prompt = basic_prompt_template(resume, user_input) # Prompt based on the user input
        response = generate(prompt) # Generates a response based on the prompt

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

def main():
    st.set_page_config(page_title="Resume Parser", page_icon="📝")
    st.title(':gray[Resume Parser] 📝🤖')
    sidebar()
    resume = file_uploader()
    if resume:
        st.expander("Resume", expanded=False).markdown(resume)
        prompt = summary_prompt_template(resume) 
        summary = generate(prompt)
        st.expander("Summary", expanded=False).markdown(summary)

        # Todo: Display the functional requirement outputs
        # st.expander("Resume Parsing", expanded=False).markdown(parsed_resume)

        # Display the chat interface with Q/A
        display_chat(resume)

if __name__ == "__main__":
    main()