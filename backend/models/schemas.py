from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    email: str
    phone: str

class BookingRequest(BaseModel):
    appointment_type: str
    date: str
    start_time: str
    patient: Patient
    reason: str
