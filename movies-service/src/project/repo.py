from datetime import timedelta, date
from bson.objectid import ObjectId
from project.db import db


class MoiveRepository():

    def __init__(self, db):
        self.db = db

    def movies(self, criteria={}):
        return [movie for movie in self.db.movies().find(criteria)]

    def movie(self, id):
        return self.db.movies().find_one({"_id": ObjectId(id)})

    def premieres(self):
        print(self.movies())
        return self.movies() #@todo -> add support for timestamp


movie_repo = MoiveRepository(db)
