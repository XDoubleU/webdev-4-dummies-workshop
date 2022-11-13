import pytest
from django.test import TestCase
from django.urls import reverse

from .models import Album, Artist


@pytest.mark.django_db
class AlbumTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artist = Artist.objects.create(
            name = "Beartooth"
        )

        cls.album = Album.objects.create(
            title = "Below",
            price = 15.99,
            record_label = "Red Bull Records"
        )
        cls.artist.albums.add(cls.album)

    def test_album_listing(self):
        assert f"{self.album.title}" == "Below"
        assert f"{self.album.artists()[0].name}" == "Beartooth"
        assert f"{self.album.price}" == "15.99"
        assert f"{self.album.record_label}" == "Red Bull Records"
    
    def test_album_list_view(self):
        response = self.client.get(reverse("album_list"))
        assert response.status_code == 200
        assert "Beartooth" in  response.rendered_content
        assert "albums/album_list.html" in [t.name for t in response.templates]

    def test_album_detail_view(self):
        response = self.client.get(self.album.get_absolute_url())
        assert response.status_code == 200
        assert "Beartooth" in response.rendered_content
        assert "albums/album_detail.html" in [t.name for t in response.templates]