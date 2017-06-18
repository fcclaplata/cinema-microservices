from datetime import timedelta, date
from project.db import db


class MoiveRepository():

    def __init__(self, db):
        self.db = db

    def movies(self):
        return {'data': self.db.movies()}

    def movie_by_id(self, id):
        return {'data': self.movies().find(lambda movie: movie.id==id)}

    def premieres(self):
        return {
            'data': [movie for movie in self.movies() if movie['releaseDate'] > (date.today() - timedelta(60))]
        }


movie_repo = MoiveRepository(db)
