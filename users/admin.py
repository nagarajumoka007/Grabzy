from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "mobile"]
    # search_fields = ['mobile']
    # list_filter = ['mobile']


admin.site.register(Profile, ProfileAdmin)
