from django.shortcuts import render


def flashcards(request):
    return render(request, "flashcards/home.html")
