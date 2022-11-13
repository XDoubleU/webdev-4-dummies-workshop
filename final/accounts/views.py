from django.views.generic import ListView
from django.db.models import Q

from albums.models import Album

class AlbumListView(ListView):
  paginate_by = 10
  model = Album
  context_object_name = "album_list"
  template_name = "albums/album_list.html"

  def get_queryset(self):
    query = self.request.GET.get("q")

    if query is None:
      return self.request.user.albums.all()

    return self.request.user.albums.filter(
      Q(title__icontains=query) | Q(artist__name__icontains=query)
    )