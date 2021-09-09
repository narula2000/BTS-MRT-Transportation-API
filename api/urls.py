from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("find_route/", views.findRoute, name="find_route"),
    path("can_reach/", views.canReach, name="can-reach")
]
