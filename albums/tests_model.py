import pytest

from albums.models import Album


@pytest.mark.django_db
def test_album_creation():
    album = Album.objects.create(artist_name="Test Artist", album_name="Test Album", year_of_release=2023, ranking=5)
    assert album.artist_name == "Test Artist"
    assert album.album_name == "Test Album"
    assert album.year_of_release == 2023
    assert album.ranking == 5
    assert str(album) == "Test Artist - Test Album"
