from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/', views.add_to_cart, name = 'add-to-cart'),
    path('', views.cart, name='cart'),
    path('details/', views.cart_details, name='cart-details'),
    path('delete/<str:pid>/', views.cart_item_delete, name='cart-item-delete'),
    path('confirm_order/', views.orders, name="confirm_order"),
    path('buy-now/<str:pid>/', views.buy_now, name='buy_now')
]