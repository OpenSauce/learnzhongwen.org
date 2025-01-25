from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("hsk/<int:level>/", views.hsk, name="hsk"),
]
