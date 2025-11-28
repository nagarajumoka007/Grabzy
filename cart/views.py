import json

from django.shortcuts import render, redirect
from django.http import  Http404, JsonResponse
from .models import Cart, Order
from django.shortcuts import get_object_or_404
from home.models import Product
from django.contrib.auth.decorators import login_required
from .utils import add_cart_item, total_cart_amount

from babel import numbers

# Create your views here.
@login_required
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pid = data.get('pid')
        sub = data.get('sub')
        cart_item_details = add_cart_item(request.user, pid, sub)
        return JsonResponse({"message": "Successful", "cart_count": request.user.user_cart.count(), 'productQuantity': cart_item_details.get('quantity'), 'productPID': cart_item_details.get('pid')})
    return Http404

# @login_required(login_url='/users/login/')
@login_required
def cart(request):
    cart_items = request.user.user_cart.all().select_related('product')
    items_count = len(cart_items)
    total_amount = sum(map(lambda x: x.product.price * x.quantity, cart_items))
    context = {
        'cart_items': cart_items,
        'items_count': items_count,
        'total_amount': total_amount
    }
    return render(request, 'cart/cart.html', context)

def cart_details(request):
    cart_count = request.user.user_cart.count()
    amount = total_cart_amount(request.user)
    amount = numbers.format_currency(amount, "INR", locale="en_IN")
    return JsonResponse({'cart_count': cart_count, 'amount': amount})

def cart_item_delete(request, pid):
    try:
        product = Product.objects.get(pid = pid)
        cart_item = request.user.user_cart.get(product=product)
        cart_item.delete()
        cart_count = cart_item = request.user.user_cart.all().count()
        return JsonResponse({'status': True, 'cart_count': cart_count})
    except(Product.DoesNotExist, Cart.DoesNotExist):
        cart_count = cart_item = request.user.user_cart.all().count()
        return JsonResponse({'status': False, 'cart_count': cart_count})
    
def orders(request):
    if request.method == 'POST':
        cart_items = request.user.user_cart.all()
        for cart_item in cart_items:
            Order.objects.create(user=request.user, product = cart_item.product, price=cart_item.product.price, quantity=cart_item.quantity)
        cart_items.delete()
        return redirect('profile')
    else:
        return Http404

def buy_now(request, pid):
    product = get_object_or_404(Product, pid=pid)
    try:
        cart_item = request.user.user_cart.get(product=product)
    except Cart.DoesNotExist:
        Cart.objects.create(user=request.user, product=product)
        cart_count = len(request.user.user_cart.all())
        return JsonResponse({"status" : "success", "cart_count" : cart_count})
    cart_count = len(request.user.user_cart.all())
    return JsonResponse({"status" : "success", "cart_count" : cart_count})