# Generated by Django 4.2.2 on 2023-06-16 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0017_alter_class_time_alter_studio_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 16, 14, 32, 39, 159260)
            ),
        ),
        migrations.AlterField(
            model_name="studio",
            name="location",
            field=models.CharField(default="21.01, 52.23", max_length=24),
        ),
    ]
