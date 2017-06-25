from pymongo import MongoClient
from os import environ

# f"mongodb://{environ.get('DBUSER')}:{environ.get('DBPWD')}@{environ.get('DBHOST')}:{environ.get('DBPORT')}{environ.get('DBPATH')}")


class Database():

    def __init__(self):
        client = MongoClient(
            f"mongodb://mongo:mongo@localhost:27017")
        db = client['admin']
        self.collection = db.movies

    def movies(self):
        return self.collection


db = Database()
