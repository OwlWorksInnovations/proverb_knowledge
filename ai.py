import os
from groq import Groq

def send_ai_request(system: str, user: str, model: str, api_key: str):
    client = Groq(
        api_key=api_key
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": user
            }
        ],
        model=model,
    )

    return chat_completion.choices[0].message.content