from django.db import models
from django.db.models import Min
from django.conf import settings


class ProductData(models.Model):
    ProductName = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
        return self.ProductName

    def get_top_image(self):
        top_image_id = self.ProductImage.all().aggregate(Min('id'))["id__min"]
        return settings.MEDIA_URL + str(self.ProductImage.filter(id=top_image_id)[0].ImageUrl)


class ProductImage(models.Model):
    ProductData = models.ForeignKey(ProductData, related_name='ProductImage', on_delete=models.CASCADE)
    ImageUrl = models.ImageField(upload_to='img_products/%Y/%m/%d')

    def __str__(self):
        return self.ProductData.ProductName + ', id:' + str(self.id)
