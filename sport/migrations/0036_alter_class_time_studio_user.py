# Generated by Django 4.2.2 on 2023-10-08 15:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0035_user_studio_owner_alter_class_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 8, 15, 11, 34, 21289)
            ),
        ),
        migrations.CreateModel(
            name="Studio_User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "studio",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="sport.studio"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]