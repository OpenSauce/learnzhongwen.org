from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class HSK(models.Model):
    level = models.IntegerField()
    character = models.CharField(max_length=1)
    pinyin = models.CharField(max_length=255)
    english = models.CharField(max_length=255)

    def __str__(self):
        return self.character


class Metric(models.Model):
    page = models.CharField(max_length=255)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.page

    def increment(self):
        self.views += 1
        self.save()
