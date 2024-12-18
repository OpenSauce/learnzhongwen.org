from django.shortcuts import render

from .models import Interest


def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def vocabulary(request):
    return render(request, "pages/vocabulary.html")


def start(request):
    return render(request, "pages/flashcards.html")


def resources(request):
    return render(request, "pages/resources.html")


def submit_email(request):
    if request.method == "POST":
        email = request.POST["email"]
        Interest.objects.create(email=email)
    return render(request, "pages/home.html")
