from django.contrib import admin
from .models import ProductData, ProductImage


class ImageInline(admin.StackedInline):
    model = ProductImage
    extra = 5


class ProductDataAdmin(admin.ModelAdmin):
    fields = ['ProductName', 'Description']
    inlines = [ImageInline]


admin.site.register(ProductData, ProductDataAdmin)
