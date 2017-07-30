from project.repo import movie_repo
from bson.json_util import dumps


def movies():
    return {'data': dumps(movie_repo.movies())}


def premieres():
    return {'data': dumps(movie_repo.premieres())}


def movie(id: str):
    return {'data': dumps(movie_repo.movie(id))}
