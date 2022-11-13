import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from albums.models import Album, Artist

@pytest.mark.django_db
class AccountTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.artist = Artist.objects.create(
      name = "Beartooth"
    )

    cls.album = Album.objects.create(
      title = "Below",
      price = "15.99",
      record_label = "Red Bull Records"
    )

    cls.artist.albums.add(cls.album)

  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username="test user",
      email="test@example.com",
      password="testpass123"
    )

    self.user.albums.add(self.album)

  def test_user_albums_list_view(self):
    self.client.login(email=self.user.email, password="testpass123")
    response = self.client.get(reverse("user_album_list"))
    assert response.status_code == 200
    assert "Below" in response.rendered_content
    assert "albums/album_list.html" in [t.name for t in response.templates]
  
  def test_login_template(self):
    response = self.client.get(reverse("account_login"))
    assert response.status_code == 200
    assert "account/login.html" in [t.name for t in response.templates]
  
  def test_signup_template(self):
    response = self.client.get(reverse("account_signup"))
    assert response.status_code == 200
    assert "account/signup.html" in [t.name for t in response.templates]