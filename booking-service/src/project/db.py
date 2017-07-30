from pymongo import MongoClient
from os import environ

DBURL = environ.get('DBURL')
DBNAME = environ.get('DBNAME')


class Database():

    def __init__(self):
        client = MongoClient(DBURL)
        db = client[DBNAME]
        self.booking_collection = db.booking
        self.tickets_collection = db.tickets

    def booking(self):
        return self.booking_collection
    
    def tickets(self):
        return self.tickets_collection


db = Database()
