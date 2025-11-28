import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Grabzy.settings")
django.setup()

from home.models import Product, Category, Vendor

# prods = Product.objects.all()
# for prod in prods:
#     print(prod.image.url)
#     prod.image.name = prod.image.name.replace("images/","")
#     prod.save()

# cats = Category.objects.all()
# for cat in cats:
#     cat.image.name = cat.image.name.replace("images/","")
#     cat.save()

# vendors = Vendor.objects.all()
# for ven in vendors:
#     ven.image.name = ven.image.name.replace("images/","")
#     ven.save()
