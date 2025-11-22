from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    mobile = models.CharField(max_length=15, unique = True)
    profile_pic = models.ImageField()


    # mobile = models.CharField(max_length=15, validators= [
    #     RegexValidator(
    #         regex= r'^\+(?:[0-9] ?){6,14}[0-9]$',
    #         message= "Please enter the valid mobile number"
    #     )
    # ])

    def __str__(self):
        return f"{self.user} {self.mobile}"