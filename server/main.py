from fastapi import FastAPI, Request
from ai import ask_ai
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to the WhatsApp AI assistant!"}

users = {}

def track_user(phone):
    users[phone] = users.get(phone, 0) + 1

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()

    phone = data.get("phone", "unknown")
    message = data.get("message", "")

    logger.info(f"Message from {phone}: {message}")

    if not message or not message.strip():
        return {"reply": "Please send me a message and I'll help you! 😊"}

    if phone:
        track_user(phone)

    reply = ask_ai(message)
    logger.info(f"AI reply to {phone}: {reply[:100]}...")

    return {"reply": reply}


@app.get("/stats")
def stats():
    return users