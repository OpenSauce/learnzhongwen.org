# Generated by Django 5.1.4 on 2024-12-17 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_metrics"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Metrics",
            new_name="Metric",
        ),
    ]
