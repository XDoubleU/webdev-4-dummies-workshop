import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse

from mollie.api.client import Client

from common.models import TimeStampedModel


class Album(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="covers/", blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    record_label = models.CharField(max_length=200)
 
    def artist(self):
        return self.artist_set.all()[0]

    def artists(self):
        return self.artist_set.all()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("album_detail", args=[str(self.id)])
    
    def get_payment_url(self, request):
        if len(settings.MOLLIE_API_KEY) < 0:
            return ""

        client = Client()
        client.set_api_key(settings.MOLLIE_API_KEY)

        payment = client.payments.create({
            'amount': {
                'currency': 'EUR',
                'value': str(self.price)
            },
            'metadata': {
                'user_id': request.user.id,
                'album_id': str(self.id)
            },
            'description': f"Payment of {self.title}",
            'redirectUrl': request.build_absolute_uri(reverse("user_album_list")),
            'webhookUrl': request.build_absolute_uri(reverse("mollie_payment"))
        })

        return payment.checkout_url



class Artist(TimeStampedModel):
    name = models.CharField(max_length=200)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.name
