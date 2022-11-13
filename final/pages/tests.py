import pytest
from django.test import SimpleTestCase
from django.urls import reverse

@pytest.mark.django_db
class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)
    
    def test_url_exists_at_correct_location(self):
        assert self.response.status_code == 200

    def test_homepage_template(self):
        assert "pages/home.html" in [t.name for t in self.response.templates]