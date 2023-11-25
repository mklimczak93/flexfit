# Generated by Django 4.2.2 on 2023-10-01 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0023_alter_class_time_remove_review_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="price",
            field=models.PositiveSmallIntegerField(default=3),
        ),
        migrations.AddField(
            model_name="user",
            name="credits",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="class",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 1, 17, 9, 59, 501624)
            ),
        ),
    ]