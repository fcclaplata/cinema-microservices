from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project import views

routes = [
    Route('/booking', 'POST', views.booking),
    Route('/booking/verify/{orderId}', 'GET', views.verify_booking)
]
