from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_view, name='search'),
    path('product/<str:pid>/', views.product_details, name='product-detail'),
    path('category/<str:cat>/', views.product_category, name='category-products'),
]