from fastapi import FastAPI, Request, HTTPException
from ai import ask_ai

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

    phone = data.get("phone")
    message = data.get("message")

    if phone:
        track_user(phone)

    reply = ask_ai(message)

    return {"reply": reply}

@app.get("/stats")
def stats():
    return users