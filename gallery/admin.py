from django.contrib import admin
from .models import GalleryImageData


class GalleryImageDataAdmin(admin.ModelAdmin):
    fields = ['ImageName', 'GalleryImage']


admin.site.register(GalleryImageData, GalleryImageDataAdmin)
