import uuid
from django.db import models
from common.models import TimeStampedModel
from django.urls import reverse


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


class Artist(TimeStampedModel):
    name = models.CharField(max_length=200)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.name
