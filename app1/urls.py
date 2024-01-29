from django.urls import path
from . import views
urlpatterns = [
    path("", views.főoldal, name="főoldal"),
    path("adatbekero/", views.adatbekérő, name="adatbekérő")
]
