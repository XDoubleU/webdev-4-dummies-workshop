from django.contrib import admin
from .models import Album, Artist

class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "cover", "price", "record_label", "artist")

class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
