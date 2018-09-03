from .models import ProductData
from django.views import generic


class ProductsTopView(generic.ListView):
    model = ProductData
    template_name = 'products/products_top.html'
    context_object_name = 'products'

    def get_queryset(self):
        """Return the last six products data."""
        return ProductData.objects.order_by('-id')[:6]


# class BlogPostView(generic.DetailView):
#     model = BlogData
#     template_name = 'blog/blog_post.html'
#     context_object_name = 'blog'
