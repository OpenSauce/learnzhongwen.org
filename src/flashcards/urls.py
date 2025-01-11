from django.urls import path

from . import views

urlpatterns = [
    path("", views.flashcards, name="flashcard_list"),
]
