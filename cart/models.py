from django.db import models
from home.models import Product
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default = 1)

    def __str__(self):
        return self.product.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="user_orders")
    oid = ShortUUIDField(prefix="ord", alphabet="123456", max_length=20, length=6, unique=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999, decimal_places=2, null=False, blank=False)
    quantity = models.PositiveSmallIntegerField(default=1, null=False, blank=False)