from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("find_route_name/", views.findRouteByName, name="find-route-name"),
    path("find_route_id/", views.findRouteById, name="find-route-id")
]
