import json

from django.shortcuts import render, redirect
from django.http import  Http404, JsonResponse, HttpResponseNotAllowed
from .models import Cart, Order
from django.shortcuts import get_object_or_404
from home.models import Product
from django.contrib.auth.decorators import login_required
from .utils import add_cart_item
from babel import numbers
from django.views.decorators.http import require_POST, require_GET
from django.db.models import F, Sum

# Create your views here.
@login_required()
@require_POST
def add_to_cart(request):
    data = json.loads(request.body or '{}')
    pid = data.get('pid')
    sub = data.get('sub')
    cart_item_details = add_cart_item(request.user, pid, sub)
    cart_count = request.user.user_cart.count()
    return JsonResponse({
        "message": "Successful", 
        "cart_count": cart_count, 
        'productQuantity': cart_item_details.get('quantity'), 
        'productPID': cart_item_details.get('pid')
    })

# @login_required(login_url='/users/login/')
@login_required()
def cart(request):
    cart_items = request.user.user_cart.select_related('product').all()
    items_count = cart_items.count()
    aggregate = cart_items.aggregate(
        total_amount = Sum(F('quantity') * F('product__price'))
    )
    print(aggregate)
    # total_amount = sum(map(lambda x: x.product.price * x.quantity, cart_items))
    context = {
        'cart_items': cart_items,
        'items_count': items_count,
        'total_amount': aggregate.get("total_amount")
    }
    return render(request, 'cart/cart.html', context)

@login_required()
@require_GET
def cart_details(request):
    cart_count = request.user.user_cart.count()
    # amount = total_cart_amount(request.user)
    amount_dict = request.user.user_cart.select_related('product').aggregate(total_amount = Sum(F('quantity') * F('product__price')))
    amount = numbers.format_currency(amount_dict.get("total_amount"), "INR", locale="en_IN")
    return JsonResponse({'cart_count': cart_count, 'amount': amount})

@login_required
@require_POST
def cart_item_delete(request, pid):
    try:
        product = Product.objects.get(pid = pid)
        cart_item = request.user.user_cart.get(product=product)
        cart_item.delete()
        cart_count = request.user.user_cart.all().count()
        return JsonResponse({'status': True, 'cart_count': cart_count})
    except(Product.DoesNotExist, Cart.DoesNotExist):
        cart_count = request.user.user_cart.all().count()
        return JsonResponse({'status': False, 'cart_count': cart_count})

    
@login_required() 
def orders(request):
    if request.method == 'POST':
        cart_items = request.user.user_cart.select_related('product').all()
        for cart_item in cart_items:
            Order.objects.create(
                user=request.user, 
                product = cart_item.product, 
                price=cart_item.product.price, 
                quantity=cart_item.quantity
            )
        cart_items.delete()
        return redirect('profile')
    else:
        raise Http404
    
@login_required()
def buy_now(request, pid):
    if request.method == 'POST':
        product = get_object_or_404(Product, pid=pid)
        try:
            cart_item = request.user.user_cart.get(product=product)
        except Cart.DoesNotExist:
            Cart.objects.create(user=request.user, product=product)
            cart_count = request.user.user_cart.all().count()
            return JsonResponse({"status" : "success", "cart_count" : cart_count})
        cart_count = request.user.user_cart.all().count()
        return JsonResponse({"status" : "success", "cart_count" : cart_count})
    else:
        cart_count = request.user.user_cart.all().count()
        return JsonResponse({"status" : "failed", "cart_count" : cart_count})