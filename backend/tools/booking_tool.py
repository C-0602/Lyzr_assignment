import requests

class BookingTool:

    @staticmethod
    def book(payload):
        res = requests.post("http://localhost:8000/api/calendly/book", json=payload)
        return res.json()
