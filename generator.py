from openai import OpenAI

from dotenv import load_dotenv

import os



load_dotenv()



client = OpenAI(

    api_key=os.getenv("GROQ_API_KEY"),

    base_url="https://api.groq.com/openai/v1"

)





SYSTEM_PROMPT = """

You are PrepAI, an AI interview preparation assistant.



Your job is to answer questions using the retrieved document context FIRST.



IMPORTANT RULES:



1. Prioritize uploaded document content whenever available.



2. If the uploaded context is incomplete or insufficient:

- use your general AI knowledge to continue the explanation

- clearly mention:

  "The following explanation includes general AI knowledge in addition to uploaded documents."



3. Keep explanations:

- clear

- structured

- beginner-friendly

- interview-focused



4. Use:

- short paragraphs

- bullet points

- examples when useful



5. Avoid:

- huge paragraphs

- markdown symbols like ** or ##

- unnecessary repetition



6. If solving a problem:

- explain step-by-step clearly.

"""







def generate_answer(query, retrieved_chunks, temperature=0.5):

    context = "\n\n".join(retrieved_chunks)



    prompt = f"""

    Retrieved Context:

    {context}



    User Question:

    {query}



    Instructions:

    - Answer clearly and professionally

    - Use uploaded content first

    - If context is insufficient, continue using general knowledge

    - Mention clearly when using general knowledge

    """



    response = client.chat.completions.create(

    model="llama-3.1-8b-instant",

    temperature=temperature,

    max_tokens=500,

    messages=[

            {

                "role": "system",

                "content": SYSTEM_PROMPT

            },

            {

                "role": "user",

                "content": prompt

            }

        ]

    )



    return response.choices[0].message.content