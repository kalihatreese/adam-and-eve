import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI
from pydantic import BaseModel
from bots.autobot import start_autobot
from bots.ashleyana_afterdark import chat_with_user

app = FastAPI()

class ChatRequest(BaseModel):
    text: str

class BotRequest(BaseModel):
    model_name: str

@app.get("/")
def root():
    return {"message": "Adam & Eve AI API is online."}

@app.post("/start_bot")
def launch_bot(req: BotRequest):
    return start_autobot(req.model_name)

@app.post("/chat")
def chat(req: ChatRequest):
    return {"reply": chat_with_user(req.text)}