from django.contrib import admin
from .models import Vendor, Category, Product, ProductImages, ProductFeatures, ProductViews

class ProducImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductFeaturesAdmin(admin.TabularInline):
    model = ProductFeatures

class ProductViewsAdmin(admin.TabularInline):
    model = ProductViews

class ProductAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'get_product_image', 'price','category', 'vendor', 'rating', 'in_stock']
    inlines = [ProducImagesAdmin, ProductFeaturesAdmin, ProductViewsAdmin]

    def short_name(self, product):
        return product.name if len(product.name) < 30 else product.name[0:30] + '...'
    
    short_name.short_description = 'Name'
    

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'mobile', 'rating', 'get_vendor_image', 'website']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_category_image']

admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Category, CategoryAdmin)