from .models import BlogData
from django.views import generic


class BlogTopView(generic.ListView):
    model = BlogData
    template_name = 'blog/blog_top.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        """Return the last five blog data."""
        return BlogData.objects.order_by('-id')[:6]


class BlogPostView(generic.DetailView):
    model = BlogData
    template_name = 'blog/blog_post.html'
    context_object_name = 'blog'
