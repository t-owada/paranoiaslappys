from django.urls import path
from toppage import views

app_name = 'toppage'
urlpatterns = [
    path('/', views.top_page, name='top_page')
]
