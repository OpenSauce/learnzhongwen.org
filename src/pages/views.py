import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

from .models import Metric


def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"],
    }

    return render(request, "pages/home.html", context)


def about(request):
    return render(request, "pages/about.html")


def vocabulary(request):
    return render(request, "pages/vocabulary.html")


def start(request):
    metric = Metric.objects.get_or_create(page="start")
    metric[0].increment()
    return render(request, "pages/resources.html")


def resources(request):
    return render(request, "pages/resources.html")
