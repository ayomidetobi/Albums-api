# Generated by Django 4.2.13 on 2024-06-29 22:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("albums", "0006_album_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="year_of_release",
            field=models.PositiveIntegerField(
                default=2000,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2100),
                ],
            ),
        ),
    ]
