# Generated by Django 5.0.6 on 2024-06-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("albums", "0005_remove_track_artist"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="genre",
            field=models.CharField(
                choices=[
                    ("rock", "Rock"),
                    ("pop", "Pop"),
                    ("jazz", "Jazz"),
                    ("classical", "Classical"),
                    ("hip_hop", "Hip Hop"),
                ],
                default="jazz",
                max_length=100,
            ),
        ),
    ]
