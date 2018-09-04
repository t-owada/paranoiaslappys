from .models import ProductData
from django.views import generic


class ProductsTopView(generic.ListView):
    model = ProductData
    template_name = 'products/products_top.html'
    context_object_name = 'products'

    def get_queryset(self):
        """Return the last six products data."""
        return ProductData.objects.order_by('-id')[:6]


class ProductDetailView(generic.DetailView):
    model = ProductData
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
