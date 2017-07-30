from datetime import timedelta, date
from bson.objectid import ObjectId
from project.db import db


class BookingRepository():

    def __init__(self, db):
        self.db = db
    
    def make_booking(self, user, booking):
        payload = {
            "city": booking["city"],
            "user_type": "loyal" if user["membership"] else "normal",
            "total_amount": booking["totalAmount"],
            "cinema": {
                "name": booking["cinema"],
                "room": booking["cinemaRoom"],
                "seats": booking["seats"]
            },
            movie: {
                "title": booking["movie"]["title"],
                "format": booking["movie"]["format"],
                "schedule": booking["schedule"]
            }
        }

        return self.db.booking().insert_one(payload)
    
    def generate_ticket(self, paid, booking):
        payload = booking
        payload["order_id"] = paid["id"]

        return self.db.tickets().insert_one(payload)
    
    def get_order_by_id(self, id):
        return self.db.booking().find_one({"_id": ObjectId(id)})


booking_repo = BookingRepository(db)
