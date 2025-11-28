from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Vendor, Product, ProductViews, ProductFeatures, ProductViews
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.http import Http404
from cart.models import Cart
import logging
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from cart.models import Order

def home(request):
    categories = Category.objects.all().order_by('?')
    popular_products = Product.objects.annotate(total_views = Count('productviews')).filter(total_views__gte = 1).order_by('-total_views')[0:10]
    logger = logging.getLogger(__name__)
    print(logger, __name__)
    logger.info("This is first Log")
    # for cat in categories:
    #     prod = Product.objects.filter(category = cat).order_by('?')[:4]
    #     data[cat] = prod
    context = {
        # "data" : data,
        "popular_products": popular_products,
        'catrgories': categories
    }
    
    if request.user.is_authenticated:
        cart_products = [item.product.pid for item in request.user.user_cart.all()]
        context = {
        # "data" : data,
        "popular_products": popular_products,
        'cart_products': cart_products,
        'catrgories': categories
        }

    return render(request, 'home/index.html', context)

def search_view(request):
    search = request.GET.get('search')
    products = Product.objects.filter(name__icontains = search) |  Product.objects.filter(category__title__contains = search)
    tag = Tag.objects.filter(name__icontains = search)
    if len(tag)>0:
        products |= Product.objects.filter(tags__in = tag)

    context = {
    'products' : products.distinct()
    }
    
    if request.user.is_authenticated:
        cart_products = [item.product.pid for item in request.user.user_cart.all()]
        context = {
        'products' : products.distinct(),
        'cart_products': cart_products
        }
    return render(request, 'home/choose-items.html', context)


def product_details(request, pid):
    product = get_object_or_404(Product, pid=pid)
    features = ProductFeatures.objects.filter(product=product)
    related_products = product.category.category_product.all().exclude(pid=product.pid).order_by('?')[:7]
    context = {
        'product': product, 
        'features': features, 
        'related_products': related_products
    }
    if request.user.is_authenticated:
        try:
            product_view = ProductViews.objects.get(product=product, user=request.user)
            print(product_view.viewed_at)
            product_view.save()
            cart_products = [item.product.pid for item in request.user.user_cart.all()]
            context = {
                'product': product, 
                'features': features, 
                'related_products': related_products,
                'cart_products': cart_products
            }

            return render(request, 'home/product.html', context)
        except ProductViews.DoesNotExist:
            pass
        print("details")
        ProductViews.objects.create(user = request.user, product = product)
        print("View Saved")
    return render(request, 'home/product.html', context)

def product_category(request, cat):
    category = get_object_or_404(Category, title=cat)
    products = category.category_product.all()
    context = {
        'products': products
    }
    if request.user.is_authenticated:
        cart_products = [item.product.pid for item in request.user.user_cart.all()]
        context = {
        'products' : products.distinct(),
        'cart_products': cart_products
        }
    return render(request, 'home/choose-items.html', context)