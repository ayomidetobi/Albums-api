from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AlbumViewSet , search_albums,TrackViewSet


router = DefaultRouter()
router.register("albums", AlbumViewSet)
router.register("tracks", TrackViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path('search/', search_albums, name='search-albums'),
]
