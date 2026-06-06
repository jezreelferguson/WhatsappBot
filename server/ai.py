import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

def ask_ai(message: str) -> str:
    """Send a message to Groq's LLM and return the AI response."""
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a friendly and helpful WhatsApp assistant to Anokye Ferguson Adu, you are a helpful assistant, you answer questions about Anokye Ferguson Adu, when he is offline, you let users know he is offline, but you are his AI Assistant, you are called FergAI. "
                    "You respond naturally and conversationally to any topic. "
                    "Keep your replies concise but informative. "
                    "Use emojis occasionally to make the conversation lively. "
                    "If you don't know something, say so honestly."
                )
            },
            {"role": "user", "content": message}
        ],
        "temperature": 0.7,
        "max_tokens": 1024,
    }

    try:
        res = requests.post(url, json=payload, headers=headers, timeout=25)
        res.raise_for_status()
        data = res.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        return "⏳ The AI is taking too long. Please try again."
    except requests.exceptions.HTTPError as e:
        print(f"Groq API HTTP Error: {e.response.status_code} - {e.response.text}")
        return "❌ AI service error. Please try again later."
    except Exception as e:
        print(f"Groq API Error: {e}")
        return "❌ Something went wrong with the AI. Please try again."