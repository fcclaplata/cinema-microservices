from pymongo import MongoClient
from os import environ


class Database():

    def __init__(self):
        client = MongoClient(
            f"mongodb://{environ.get('DBUSER')}:{environ.get('DBPWD')}@{environ.get('DBHOST')}:{environ.get('DBPORT')}{environ.get('DBPATH')}")
        db = client[environ.get('DBNAME')]
        self.collection = db.movies

    def movies(self):
        return self.collection

db = Database()
