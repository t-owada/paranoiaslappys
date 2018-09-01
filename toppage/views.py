from django.shortcuts import render
from django.http import HttpResponse
from toppage.models import TopPageContent


def top_page(request):
    top_page_content = TopPageContent.objects.last()
    return render(request, 'toppage/top_page.html', {'TopPageContent': top_page_content})
