from pymongo import MongoClient
from os import environ


DBNAME = environ.get('DBNAME')
DBURL = environ.get('DBURL')

# DBUSER = environ.get('DBUSER')
# DBPWD = environ.get('DBPWD')
# DBHOST = environ.get('DBHOST')
# DBPORT = environ.get('DBPORT')


class Database():

    def __init__(self):
        # client = MongoClient(f"mongodb://{DBUSER}:{DBPWD}@{DBHOST}:{DBPORT}")
        client = MongoClient(DBURL)
        print(DBNAME)
        self.db = client[DBNAME]

    @property
    def cinemas(self):
        return self.db.cinemas

    @property
    def cities(self):
        return self.db.cities

    @property
    def states(self):
        return self.db.states

    @property
    def countries(self):
        return self.db.countries


db = Database()
