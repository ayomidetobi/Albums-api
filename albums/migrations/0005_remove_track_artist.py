# Generated by Django 5.0.6 on 2024-06-25 19:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("albums", "0004_album_description_album_duration_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="track",
            name="artist",
        ),
    ]
