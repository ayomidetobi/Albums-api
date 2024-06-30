import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from albums.models import Album


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="testpass")


@pytest.fixture
def token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token


@pytest.mark.django_db
def test_album_list(api_client, user, token):
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    url = reverse("album-list")
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_album(api_client, user, token):
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    url = reverse("album-list")
    data = {
        "artist_name": "New Artist",
        "album_name": "New Album",
        "year_of_release": 2024,
        "ranking": 4,
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert Album.objects.count() == 1
    assert Album.objects.get().artist_name == "New Artist"


@pytest.mark.django_db
def test_album_detail(api_client, user, token):
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    album = Album.objects.create(
        artist_name="Test Artist",
        album_name="Test Album",
        year_of_release=2023,
        ranking=5,
    )
    url = reverse("album-detail", args=[album.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data["artist_name"] == "Test Artist"


@pytest.mark.django_db
def test_update_album(api_client, user, token):
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    album = Album.objects.create(
        artist_name="Test Artist",
        album_name="Test Album",
        year_of_release=2023,
        ranking=5,
    )
    url = reverse("album-detail", args=[album.id])
    data = {
        "artist_name": "Updated Artist",
        "album_name": "Updated Album",
        "year_of_release": 2024,
        "ranking": 4,
    }
    response = api_client.put(url, data, format="json")
    assert response.status_code == 200
    album.refresh_from_db()
    assert album.artist_name == "Updated Artist"


@pytest.mark.django_db
def test_delete_album(api_client, user, token):
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    album = Album.objects.create(
        artist_name="Test Artist",
        album_name="Test Album",
        year_of_release=2023,
        ranking=5,
    )
    url = reverse("album-detail", args=[album.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Album.objects.count() == 0
