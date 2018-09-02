from .models import GalleryImageData
from django.views import generic


class GalleryView(generic.ListView):
    model = GalleryImageData
    template_name = 'gallery/gallery.html'
    context_object_name = 'gallery_images'

    def get_queryset(self):
        """Return the last 12 gallery images."""
        return GalleryImageData.objects.order_by('-id')[:12]
