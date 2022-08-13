from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Album


class AlbumListView(ListView):
    paginate_by = 10
    model = Album
    context_object_name = "album_list"
    template_name = "albums/album_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        
        if query is None:
            return self.model.objects.all()
 
        return self.model.objects.filter(
            Q(title__icontains=query) | Q(artist__name__icontains=query)
        )

class AlbumDetailView(DetailView):
    model = Album
    context_object_name = "album"
    template_name = "albums/album_detail.html"
