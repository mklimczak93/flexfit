# Generated by Django 4.2.2 on 2023-06-15 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0010_alter_class_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 15, 16, 25, 44, 93078)
            ),
        ),
    ]
