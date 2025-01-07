from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(
        max_length=200, unique=True, help_text="Title of the post"
    )
    content = models.TextField(help_text="Markdown supported content")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="Author of the post"
    )
    published = models.BooleanField(
        default=False, help_text="Is the post published?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Date and time of creation"
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Date and time of last update"
    )

    class Meta:
        ordering = ["-created_at"]

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
