# Generated by Django 4.2.2 on 2023-06-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="studio",
            name="studio_type",
            field=models.CharField(default="", max_length=60),
        ),
    ]