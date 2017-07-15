from pymongo import MongoClient
from os import environ

DBURL = environ.get('DBURL')
DBNAME = environ.get('DBNAME')


class Database():

    def __init__(self):
        client = MongoClient(DBURL)
        db = client[DBNAME]
        self.collection = db.movies

    def movies(self):
        return self.collection


db = Database()
