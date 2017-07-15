from pymongo import MongoClient
from os import environ

DBUSER = environ.get('DBUSER')
DBPWD = environ.get('DBPWD')
DBHOST = environ.get('DBHOST')
DBPORT = environ.get('DBPORT')
DBNAME = environ.get('DBNAME')


class Database():

    def __init__(self):
        client = MongoClient(f"mongodb://{DBUSER}:{DBPWD}@{DBHOST}:{DBPORT}")
        db = client[DBNAME]
        self.collection = db.movies

    def movies(self):
        return self.collection


db = Database()
