from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

from pages import views

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path("resources/", views.resources, name="resources"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
