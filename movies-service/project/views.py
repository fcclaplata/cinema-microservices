from project.repo import movie_repo


def movies():
    return {'data': movie_repo.movies()}


def premieres():
    return {'data': movie_repo.premieres()}


def movie(id: str):
    return {'data': movie_repo.movie(id)}
