# Generated by Django 5.1.4 on 2024-12-17 21:03

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_rename_metrics_metric"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="metric",
            name="date",
        ),
        migrations.AlterField(
            model_name="metric",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]
