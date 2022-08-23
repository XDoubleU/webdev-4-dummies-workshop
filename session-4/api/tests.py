import mock
import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from mollie.api.resources.payments import Payments
from mollie.api.objects.payment import Payment

from albums.models import Album, Artist


@pytest.mark.django_db
class ApiTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test user", 
            email="test@example.com",
            password="testpass123"
        )

        cls.artist = Artist.objects.create(
            name = "Beartooth"
        )
        cls.album = Album.objects.create(
            title = "Below",
            price = "15.99",
            record_label = "Red Bull Records"
        )

        cls.artist.albums.add(cls.album)

    @mock.patch.object(Payments, 'get', autospec=True)
    def test_mollie_payment_webhook(self, mock_payments_get):
        payment_data = {
            'paidAt': 'now',
            'metadata': {
                'userid': self.user.id,
                'albumid': self.album.id
            }
        }

        mock_payments_get.return_value = Payment(payment_data)
        data = {
            'id': 'tr_thisisanid'
        }

        response = self.client.post(reverse("mollie_payment"), data)

        assert response.status_code == 200
        assert self.user.albums.all()[0].title == "Below"

