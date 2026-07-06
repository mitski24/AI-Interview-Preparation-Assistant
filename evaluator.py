from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)



def evaluate_answer(question, answer):
    prompt = f"""
You are an interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Evaluate:
1. Correctness
2. Clarity
3. Completeness

Return:
- Score out of 10
- Strengths
- Weaknesses
- Suggestions
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content