from django.db import models


class FlashcardContent(models.Model):
    hsk_level = models.IntegerField()
    simplified = models.TextField()
    radical = models.TextField()
    frequency = models.IntegerField()
    pos = models.JSONField(default=list)
    traditional = models.TextField()
    pinyin = models.TextField()
    numeric_pinyin = models.TextField()
    wade_giles = models.TextField()
    bopomofo = models.TextField()
    romatzyh = models.TextField()
    meanings = models.JSONField(default=list)
    classifiers = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("hsk_level", "simplified", "pinyin")

    def __str__(self):
        return f"{self.simplified} ({self.pinyin}) - HSK {self.hsk_level}"
