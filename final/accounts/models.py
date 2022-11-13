from django.db import models
from django.contrib.auth.models import AbstractUser
from albums.models import Album

class CustomUser(AbstractUser):
  albums = models.ManyToManyField(Album)
