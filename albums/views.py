from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from .models import Album, Track
from .serializers import AlbumSerializer, TrackSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.db.models import Q


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = TrackSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def search_albums(request):
    query = request.query_params.get("q", None)
    if query:
        albums = Album.objects.filter(
            Q(album_name__icontains=query) | Q(artist_name__icontains=query)
        )
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)
    return Response({"albums": []})
