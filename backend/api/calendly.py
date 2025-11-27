from fastapi import APIRouter, HTTPException
import json

router = APIRouter()

with open("data/doctor_schedule.json") as f:
    schedule = json.load(f)

@router.get("/calendly/availability")
def get_availability(date: str, appointment_type: str):
    if date not in schedule:
        raise HTTPException(404, "Date not found")
    return {"date": date, "available_slots": schedule[date]["slots"]}

@router.post("/calendly/book")
def book(body: dict):
    date = body["date"]
    start = body["start_time"]

    if date not in schedule:
        raise HTTPException(404, "Invalid date")

    for slot in schedule[date]["slots"]:
        if slot["start_time"] == start:
            if not slot["available"]:
                raise HTTPException(400, "Slot already booked")
            slot["available"] = False
            return {"status": "confirmed", "booking_id": "CONFIRM-001", "details": body}

    raise HTTPException(404, "Slot not found")
