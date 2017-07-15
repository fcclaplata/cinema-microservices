from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project import views

routes = [
    Route('/', 'GET', views.cinemas),
    Route('/{cinema_id}', 'GET', view.cinema),
    Route('/{cinema_id}/{movie_id}', 'GET', views.schedules),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]
document into the cinema document.
