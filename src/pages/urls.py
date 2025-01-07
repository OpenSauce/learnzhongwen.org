from django.contrib.sitemaps.views import sitemap
from django.urls import path

from pages import views

from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", views.home, name="home"),
    path("start/", views.start, name="start"),
    path("start/submit-email/", views.submit_email, name="submit_email"),
    path("about/", views.about, name="about"),
    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path("resources/", views.resources, name="resources"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
]
