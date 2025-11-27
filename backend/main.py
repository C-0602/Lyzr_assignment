from fastapi import FastAPI
from backend.api.chat import router as chat_router
from backend.api.calendly import router as calendly_router

app = FastAPI(title="Medical Scheduling Agent")

app.include_router(chat_router, prefix="/api")
app.include_router(calendly_router, prefix="/api")
