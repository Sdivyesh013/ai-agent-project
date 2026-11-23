import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq

load_dotenv()

app = FastAPI()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Hello! The FAQ bot server is running."}

@app.get("/about")
def about():
    return {"bot": "Company FAQ Assistant", "status": "learning", "version": 1,"groq_key_loaded": os.getenv("GROQ_API_KEY") is not None}

@app.post("/chat")
def chat(data: ChatRequest):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": data.message}],
    )
    answer = response.choices[0].message.content
    return {"reply": answer}