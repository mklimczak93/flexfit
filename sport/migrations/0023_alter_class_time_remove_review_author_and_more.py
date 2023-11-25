# Generated by Django 4.2.2 on 2023-09-30 14:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sport", "0022_alter_class_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 30, 14, 46, 10, 645380)
            ),
        ),
        migrations.RemoveField(
            model_name="review",
            name="author",
        ),
        migrations.AlterField(
            model_name="review",
            name="class_rated",
            field=models.ForeignKey(
                db_constraint=False,
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="class_rated",
                to="sport.class",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="author",
            field=models.ForeignKey(
                db_constraint=False,
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="review_author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]