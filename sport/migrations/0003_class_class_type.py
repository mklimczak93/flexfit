# Generated by Django 4.2.2 on 2023-06-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0002_studio_studio_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="class_type",
            field=models.CharField(default="", max_length=60),
        ),
    ]
