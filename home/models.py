import os
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

mobile_validator = RegexValidator(
    regex = r'^\+?(?:[0-9] ?){6,14}[0-9]$',
    message = 'Invalid mobile numebr'
)

email_validator = RegexValidator(
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$',
    message = 'Invalid email'
)

rating_validators = [
    MinValueValidator(0),
    MaxValueValidator(5)
    
]


class Category(models.Model):
    cid = ShortUUIDField(max_length=20, length=6, alphabet='abcde123456', prefix='cat', unique=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/category', default='images/default.png')
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
    def get_category_image(self):
        return mark_safe(f"<img src='{self.image.url}' alt='category image' width='50' height='50'>")

class Vendor(models.Model):
    vid = ShortUUIDField(max_length=20, length=6, alphabet='abcde123456', prefix='ven', unique=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/vendor', default = 'images/default.png')
    email = models.EmailField(unique=True, validators=[email_validator])
    mobile = models.CharField(validators=[mobile_validator])
    address = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=rating_validators, blank=True, null=True)
    website = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.title
    
    def get_vendor_image(self):
        return mark_safe(f"<img src={self.image.url} alt='vendor image' width='50' height='50'>")

class Product(models.Model):
    pid = ShortUUIDField(unique=True, max_length=20, length=6, alphabet='abcde123456', prefix='prd')
    name = models.CharField()
    description = models.TextField()
    image = models.ImageField(upload_to="images/products", default='images/default.png')
    price = models.DecimalField(max_digits=999999999, decimal_places=2)
    old_price = models.DecimalField(max_digits=999999999, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=rating_validators, blank=True, null=True)
    in_stock = models.BooleanField(default=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, related_name="category_product", on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length = 300, unique=True, null=True, blank=True)
    tags = TaggableManager(blank=None)
    
    # class Meta:
    #     verbose_name_plural = 'Products'

    def __str__(self):
        return self.name if len(self.name) < 30 else self.name[0:30] + '...'
    
    def get_product_image(self):
        return mark_safe(f"<img src={self.image.url} alt='product image' width='50', height = '50'>")
    
    def get_offer_percentage(self):
        percentage = (self.old_price - self.price)// self.old_price
        print(percentage)
        return f"{percentage}%"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)

        try:
            OldProduct = Product.objects.get(pid = self.pid)
            if OldProduct.image.url != self.image.url and self.image.url:
                if os.path.isfile(OldProduct.image.url):
                    os.remove(OldProduct.image.url)
        except Product.DoesNotExist:
            pass

        super().save(*args, **kwargs)

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/products')


class ProductFeatures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)
    feature_value = models.CharField(max_length=300)

class ProductViews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product} viewed by {self.user} at {self.viewed_at}"