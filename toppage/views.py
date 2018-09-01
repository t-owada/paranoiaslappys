from django.shortcuts import render
from django.http import HttpResponse
from .models import TopPageContent
from django.views import generic


def TopPageView(request):
    top_page_content = TopPageContent.objects.last()
    return render(request, 'toppage/top_page.html', {'TopPageContent': top_page_content})
