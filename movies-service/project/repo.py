from datetime import timedelta, date
from bson.objectid import ObjectId
from project.db import db


class MoiveRepository():

    def __init__(self, db):
        self.db = db

    def movies(self):
        return [movie for movie in self.db.movies().find()]

    def movie(self, id):
        return self.db.movies().find_one({"_id": ObjectId(id)})

    def premieres(self):
        print(self.movies())
        return [movie for movie in self.movies() if date.fromtimestamp(movie['releaseDate']) > (date.today() - timedelta(60))]


movie_repo = MoiveRepository(db)
