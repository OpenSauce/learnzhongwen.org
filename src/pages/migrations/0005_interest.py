# Generated by Django 5.1.4 on 2024-12-18 20:56

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_remove_metric_date_alter_metric_views"),
    ]

    operations = [
        migrations.CreateModel(
            name="Interest",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
