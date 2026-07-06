from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

api_key = os.getenv("GROQ_API_KEY")

print("Loaded Key:", api_key)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Explain DBMS simply"
        }
    ]
)

print(response.choices[0].message.content)