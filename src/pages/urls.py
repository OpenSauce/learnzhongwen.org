from django.urls import path

from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path("resources/", views.resources, name="resources"),
]
