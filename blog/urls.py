from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogTopView.as_view(), name='blog_top'),
]
