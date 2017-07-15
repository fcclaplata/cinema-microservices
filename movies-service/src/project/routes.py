from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project import views

routes = [
    Route('/', 'GET', views.movies),
    Route('/premieres', 'GET', views.premieres),
    Route('/{id}', 'GET', views.movie),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]
