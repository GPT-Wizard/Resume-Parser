import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from src.ui import sidebar, file_uploader
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(api_key=os.environ.get("OPENAI_API_KEY"), model="gpt-3.5-turbo-16k")

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a AI assistant for an recruiter to understand about an candidate's resume. Your task is to answer the questions by the user based only on the candidate resume."),
    ("user", """
    Resume Details:
    {resume}
    Recruiters Question:
    {question}
    Answer:
    """)
])

qa_generation_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class technical recruiter. Your task is to ask questions based on the job description to evaluate the candidate's resume."),
    ("user", """Ask questions based on the job description to evaluate the candidate's resume:
    Job Description:
    {job_description}
    Resume Details:
    {resume}
    """)
])

resume_parser_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class technical text parser. Your task is to convert resume details into a well-structured JSON formatted output with key-value pairs."),
    ("user", """Convert the following resume details into a JSON formatted output:
    Resume Details:
     ```
     {resume}
     ```
    JSON output should be structured key-value pairs with the following fields:
    Name, Email, Phone, Address, Summary, Experience, Education, Skills, Certifications, Projects, Others, etc.
    JSON Output:
    """)
])

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

        chain = qa_prompt | llm   
        response = chain.invoke({"input": user_input})      

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
        
        resume_parser_chain = resume_parser_prompt | llm | StrOutputParser()
        qa_generation_chain = qa_generation_prompt | llm | StrOutputParser()

        main_chain = RunnableParallel({"qa_set": qa_generation_chain, "parsed": resume_parser_chain})
        result = main_chain.invoke({"job_description": job_description, "resume": resume})

        st.expander("Parsed", expanded=False).json(result["parsed"])
        st.expander("Q/A Generation", expanded=False).markdown(result["qa_set"])
        # Todo: Display the functional requirement outputs

        # Display the chat interface with Q/A
        display_chat(resume)

if __name__ == "__main__":
    main()