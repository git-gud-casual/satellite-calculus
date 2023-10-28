from django.urls import path

from pictures import views

urlpatterns = [
    path("", views.ListPicturesView.as_view())
]
