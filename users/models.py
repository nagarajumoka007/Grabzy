from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    mobile = models.CharField(max_length=15, unique = True)
    profile_pic = models.ImageField(upload_to="profile/", default="profile/default-user.webp")


    # mobile = models.CharField(max_length=15, validators= [
    #     RegexValidator(
    #         regex= r'^\+(?:[0-9] ?){6,14}[0-9]$',
    #         message= "Please enter the valid mobile number"
    #     )
    # ])

    def __str__(self):
        return f"{self.user} {self.mobile}"
    
    def save(self, *args, **kwargs):
        try:
            old = Profile.objects.get(pk = self.pk).profile_pic
            print("Old", old)
        except Profile.DoesNotExist:
            old = None
        
        super().save(*args, **kwargs)
        print("Old.name", old.name)
        print("media_url", settings.MEDIA_ROOT)
        if old and old != self.profile_pic and old.name != "profile/default-user.webp":
            path = os.path.join(settings.MEDIA_ROOT, old.name)
            if os.path.exists(path):
                os.remove(path)