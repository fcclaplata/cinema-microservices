from .repo import movie_repo
from bson.json_util import dumps


def cinemas():
    movie_repo.cinemas()


def cinema(cinema_id: str):
    movie_repo.cinema(cinema_id)


def schedules(city_id: str, movie_id: str):
    movie_repo.schedules(city_id, movie_id)
