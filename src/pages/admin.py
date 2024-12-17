from django.contrib import admin

from .models import HSK, Post, Metric

admin.site.register(Post)
admin.site.register(HSK)
admin.site.register(Metric)