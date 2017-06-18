from project.repo import movie_repo


def movies():
    return movie_repo.movies()


def premieres():
    return movie_repo.premieres()


def movie(id: int):
    return movie_repo.movie(id)
