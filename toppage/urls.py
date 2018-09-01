from django.urls import path
from . import views

app_name = 'toppage'
urlpatterns = [
    path('', views.TopPageView, name='top_page')
]
