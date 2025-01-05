from django.db import models
from django.utils import timezone


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


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Interest(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
