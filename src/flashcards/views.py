from django.shortcuts import render

from .models import FlashcardContent


def landing(request):
    levels = [
        {
            "level": 1,
            "description": (
                "Basic vocabulary for beginners. "
                "Perfect for starting your journey."
            ),
        },
        {
            "level": 2,
            "description": "Expand your vocabulary with everyday words.",
        },
        {
            "level": 3,
            "description": (
                "Intermediate vocabulary for daily conversations "
                "and basic topics."
            ),
        },
        {
            "level": 4,
            "description": (
                "Advanced topics and vocabulary for in-depth discussions."
            ),
        },
        {
            "level": 5,
            "description": (
                "Master complex vocabulary and refine your fluency."
            ),
        },
    ]
    return render(request, "flashcards/landing.html", {"levels": levels})


def hsk(request, level):
    flashcards = FlashcardContent.objects.filter(hsk_level=level)
    return render(
        request,
        "flashcards/hsk.html",
        {"flashcards": flashcards, "hsk_level": level},
    )
