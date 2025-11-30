from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Vendor, Product, ProductViews, ProductFeatures
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.http import Http404
from cart.models import Cart
import logging
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Q
from cart.models import Order

logger = logging.getLogger(__name__)

def home(request):
    categories = Category.objects.all().order_by('?')
    popular_products = Product.objects.annotate(total_views = Count('productviews')).filter(total_views__gte = 1).order_by('-total_views')[0:10]
    logger.info("This is first Log")
    context = {
        "popular_products": popular_products,
        'categories': categories
    }
    
    if request.user.is_authenticated:
        context = {
        "popular_products": popular_products,
        'categories': categories
        }
    return render(request, 'home/index.html', context)

def search_view(request):
    search = request.GET.get('search')
    products = Product.objects.filter(Q(name__icontains = search) | Q(category__title__contains = search) | Q(tags__name__icontains = search))

    context = {
    'products' : products.distinct()
    }
    
    if request.user.is_authenticated:
        context = {
        'products' : products.distinct(),
        }
    return render(request, 'home/choose-items.html', context)


def product_details(request, pid):
    product = get_object_or_404(Product, pid=pid)
    features = ProductFeatures.objects.filter(product=product)
    related_products = product.category.category_product.select_related('category', 'vendor').all().exclude(pid=product.pid).order_by('?')[:7]
    context = {
        'product': product, 
        'features': features, 
        'related_products': related_products
    }
    if request.user.is_authenticated:
        try:
            product_view = ProductViews.objects.update_or_create(product=product, user=request.user, defaults= {'viewed_at': timezone.now()})
            context = {
                'product': product, 
                'features': features, 
                'related_products': related_products,
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
    products = category.category_product.select_related('category', 'vendor').all()
    context = {
        'products': products
    }
    if request.user.is_authenticated:
        context = {
        'products' : products.distinct(),
        }
    return render(request, 'home/choose-items.html', context)