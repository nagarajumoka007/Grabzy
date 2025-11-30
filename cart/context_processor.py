from .models import Cart
from django.contrib.auth.models import User

def default(request):
    if request.user.is_authenticated:
        count = request.user.user_cart.all().count()
        user_cart =  {item.product.pid : item for item in request.user.user_cart.select_related('product').all()}
        cart_products = [item.product.pid for item in request.user.user_cart.all()]
    else:
        count = 0
        user_cart = None
        cart_products = []
    
    return {'Cart_Count': count, 'user_cart': user_cart, 'cart_products': cart_products}