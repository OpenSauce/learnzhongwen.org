from django.db import models


class HSK(models.Model):
    level = models.IntegerField()
    character = models.CharField(max_length=1)
    pinyin = models.CharField(max_length=255)
    english = models.CharField(max_length=255)

    def __str__(self):
        return self.character
