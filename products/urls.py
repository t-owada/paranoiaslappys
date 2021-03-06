from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductsTopView.as_view(), name='products_top'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]
