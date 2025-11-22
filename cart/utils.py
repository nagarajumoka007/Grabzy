from urllib.parse  import urlparse, parse_qs, urlencode, urlunparse

from .models import Cart
from home.models import Product
from django.shortcuts import get_object_or_404

def add_cart_item(user, productPID, sub=False): 
    product = get_object_or_404(Product, pid=productPID)
    try:
        print("fetching cart")
        cart_item = user.user_cart.get(product = product)
        print('cart', cart_item)
        if sub == True:
            cart_item.quantity -= 1
            if cart_item.quantity == 0:
                cart_item.delete()
                return {'pid': productPID, 'quantity': 0}
            cart_item.save()
            return {'pid': productPID, 'quantity': cart_item.quantity}
        else:
            cart_item.quantity +=1
            cart_item.save()
            return {'pid': productPID, 'quantity': cart_item.quantity}
    except Cart.DoesNotExist:
        cart_item = Cart.objects.create(user = user, product = product)
        return {'pid': productPID, 'quantity': cart_item.quantity}
    
def add_paramters_to_url(url, params):
    new_url = urlparse(url)
    query_params = parse_qs(new_url.query)
    query_params.update(params)
    query_string = urlencode(query_params, doseq=True)
    final_url = urlunparse(new_url._replace(query=query_string))
    print(final_url)
    return final_url

def total_cart_amount(user):
    amount = 0
    cart_items = user.user_cart.all()
    for item in cart_items:
        amount += (item.quantity * item.product.price)
        print("quantity",item.quantity, "price", int(item.product.price))
        print("total amount", amount)
    return amount