import requests

class AvailabilityTool:

    @staticmethod
    def get(date, appt_type):
        res = requests.get(
            "http://localhost:8000/api/calendly/availability",
            params={"date": date, "appointment_type": appt_type},
        )
        return res.json()
