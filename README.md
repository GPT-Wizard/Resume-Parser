# Building a Generative AI Application: Resume Parser 📝🤖

## Introduction 🌟
> We will build a Generative AI application using a Large Language Model (LLM) to parse resumes. Leveraging our knowledge of LLMs and the technique of prompt engineering, we will develop a system that can extract and structure information from resumes, score them based on job descriptions, mask personal information, and generate interview questions.

## Problem Statement ❓
> Objective: Create an application that parses uploaded resumes, extracts and structures the content, and provides additional functionalities to enhance the evaluation process.

## Requirements ✅
- Python 3.7 or above
- [Get an openai API key](https://platform.openai.com/account/api-keys)

## Run The Application ⚙️

### 1. Clone the repo
```
git clone https://github.com/GPT-Wizard/Resume-Parser.git
```

### 2. Install packages
If running for the first time,

- Create virtual environment
```
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
```

- Install required libraries
```
pip3 install -r requirements.txt
```


### 3. Set up your API key
Set your API keys in the `.env` file by copying `.env.example`

### 4. Running
```
streamlit run app.py 
```
