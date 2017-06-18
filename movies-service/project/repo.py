from datetime import timedelta, date
from project.db import db


class MoiveRepository():

    def __init__(self, db):
        self.db = db

    def movies(self):
        return self.db.movies()

    def movie(self, id):
        for movie in self.movies():
            if movie['id'] == str(id):
                return movie
        raise NotImplementedError

    def premieres(self):
        print(self.movies())
        return [movie for movie in self.movies() if date.fromtimestamp(movie['releaseDate']) > (date.today() - timedelta(60))]


movie_repo = MoiveRepository(db)
