from django.db import models


class GalleryImageData(models.Model):
    ImageName = models.CharField(max_length=255)
    GalleryImage = models.ImageField(null=True, blank=True, upload_to='img_gallery/%Y/%m/%d')

    def __str__(self):
        return self.ImageName
