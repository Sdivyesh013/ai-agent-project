from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Hello! The FAQ bot server is running."}

@app.get("/about")
def about():
    return {"bot": "Company FAQ Assistant", "status": "learning", "version": 1}

@app.post("/chat")
def chat(data: ChatRequest):
    return {"reply": data.message}