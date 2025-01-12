from django.contrib import admin

from .models import FlashcardContent


@admin.register(FlashcardContent)
class FlashcardContentAdmin(admin.ModelAdmin):
    list_display = ("simplified", "pinyin", "hsk_level", "frequency")
    search_fields = ("simplified", "pinyin")
    list_filter = ["hsk_level"]
    readonly_fields = ("created_at",)  # Make `created_at` read-only

    fieldsets = (
        (None, {"fields": ("simplified", "pinyin", "hsk_level")}),
        (
            "Details",
            {
                "fields": (
                    "radical",
                    "frequency",
                    "pos",
                    "meanings",
                    "classifiers",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at",),
            },
        ),
    )
