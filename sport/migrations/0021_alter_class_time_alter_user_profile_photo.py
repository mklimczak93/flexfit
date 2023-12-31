# Generated by Django 4.2.2 on 2023-08-20 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0020_rename_name_studio_studio_name_studio_owner_fr_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 20, 19, 6, 45, 460153)
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(
                default="user_profiles/MockupPhoto01.png", upload_to="user_profiles"
            ),
        ),
    ]
