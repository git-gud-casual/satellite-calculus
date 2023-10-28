from django.urls import path

from satellites import views

urlpatterns = [
    path("by_zone", views.SatelliteByZone.as_view())
]
