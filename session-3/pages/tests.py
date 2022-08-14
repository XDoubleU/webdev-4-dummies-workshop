import pytest
from django.test import SimpleTestCase
from django.urls import reverse

@pytest.mark.django_db
class HomePageTests(SimpleTestCase):
    def setUp(self):
        # Arrange
        url = reverse("home")
        # Act
        self.response = self.client.get(url)
        
    def test_url_exists_at_correct_location(self):
        # self.assertEqual(self.response.status_code, 200)
        # option above is used frequently in Django, better to use option below when using pytest
        # Assert
        assert self.response.status_code == 200
    
    def test_homepage_template(self):
        # self.assertTemplateUsed(self.response, "pages/home.html")
        # same remark as before
        assert "pages/home.html" in [x.name for x in self.response.templates]
