from .models import Cart
from django.contrib.auth.models import User

def default(request):
    if request.user.is_authenticated:
        count = len(request.user.user_cart.all())
        print(count)
        user_cart =  {item.product.pid : item for item in request.user.user_cart.all()}
    else:
        count = 0
        user_cart = None
    
    return {'Cart_Count': count, 'user_cart': user_cart}