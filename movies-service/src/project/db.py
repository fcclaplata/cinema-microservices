from pymongo import MongoClient
from os import environ

DBURL = environ.get('DBURL')


class Database():

    def __init__(self):
        client = MongoClient(DBURL)
        db = client
        self.collection = db.movies

    def movies(self):
        return self.collection


db = Database()
