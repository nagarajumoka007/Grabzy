from django.contrib.auth.backends import ModelBackend
from .models import Profile
from django.contrib.auth.models import User

class MobileAuthenticationBackend(ModelBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):
        mobile = kwargs.get("mobile")
        user = None
        try:
            if mobile:
                profile = Profile.objects.get(mobile=mobile)
                user = profile.user
            elif username:
                user = User.objects.get(username = username)
        except (Profile.DoesNotExist, User.DoesNotExist):
            return None
        
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        return None