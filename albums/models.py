from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pymongo import MongoClient
class Album(models.Model):
    GENRE_CHOICES = [
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('hip_hop', 'Hip Hop'),
    ]
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    year_of_release = models.PositiveIntegerField(default=2000)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default='jazz')
    ranking = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    album_cover = models.ImageField(upload_to="album_covers/", null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return f"{self.artist_name} - {self.album_name}"

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.name} in {self.album.album_name}"