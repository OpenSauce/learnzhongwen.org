# Generated by Django 5.1.4 on 2025-01-05 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0006_remove_interest_created_at_interest_created_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="interest",
            name="created",
        ),
    ]
