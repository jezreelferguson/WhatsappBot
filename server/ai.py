import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

def ask_ai(message: str):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful WhatsApp assistant. Keep replies short and clear."
            },
            {"role": "user", "content": message}
        ]
    }

    res = requests.post(url, json=payload, headers=headers)
    return res.json()["choices"][0]["message"]["content"]