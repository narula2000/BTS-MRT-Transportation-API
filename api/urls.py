from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("all_routes/", views.allRoutes, name="all-routes")
]
