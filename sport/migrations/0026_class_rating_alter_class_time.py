# Generated by Django 4.2.2 on 2023-10-03 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0025_alter_class_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="rating",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="class",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 3, 13, 42, 10, 787846)
            ),
        ),
    ]
