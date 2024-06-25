from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

from .models import Album,Track


class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name"]

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields ='__all__'

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    
    class Meta:
        model = Album
        fields = ['id', 'artist_name', 'album_name', 'year_of_release','genre', 'ranking', 'album_cover', 'tracks']
