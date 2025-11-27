from fastapi import APIRouter
from pydantic import BaseModel
from backend.agent.scheduling_agent import SchedulingAgent

router = APIRouter()
agent = SchedulingAgent()

class ChatMessage(BaseModel):
    user_message: str
    session_id: str = "default"

@router.post("/chat")
async def chat(msg: ChatMessage):
    return {"response": await agent.handle_message(msg.session_id, msg.user_message)}
