from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("find_route_name/", views.findRouteByName, name="find-route-name"),
    path("find_route_id/", views.findRouteById, name="find-route-id"),
    path("get_station_name/", views.getStationNameById, name="get-station-name"),
    path("get_station_id/", views.getStationIdByName, name="get-station-id")
]
