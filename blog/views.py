from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogData
from  django.views import generic


class BlogTopView(generic.ListView):
    model = BlogData
    paginate_by = 5
    template_name = 'blog/blog_top.html'
    context_object_name = 'blogs'
