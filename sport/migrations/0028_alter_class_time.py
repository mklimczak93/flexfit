# Generated by Django 4.2.2 on 2023-10-03 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0027_class_rat_amount_alter_class_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 3, 13, 47, 22, 946827)
            ),
        ),
    ]