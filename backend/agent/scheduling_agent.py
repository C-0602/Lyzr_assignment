import openai, os
from backend.rag.faq_rag import FAQ_RAG
from backend.tools.availability_tool import AvailabilityTool
from backend.tools.booking_tool import BookingTool
from backend.agent.prompts import SYSTEM_PROMPT

class SchedulingAgent:

    def __init__(self):
        self.rag = FAQ_RAG()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def handle_message(self, sid, msg):

        # FAQ handling
        if any(x in msg.lower() for x in ["insurance", "policy", "parking", "hours"]):
            return self.rag.query(msg)

        # LLM scheduling flow
        completion = openai.ChatCompletion.create(
            model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": msg},
            ],
        )
        return completion["choices"][0]["message"]["content"]
