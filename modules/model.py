from openai import OpenAI
import os
from dotenv import load_dotenv
# Load configs from .env file
load_dotenv()

llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate(prompt):
    response = llm.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo", 
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content



