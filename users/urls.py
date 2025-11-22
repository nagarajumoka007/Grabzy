from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='user-login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='user-logout'),
    path('profile/', views.profile, name="profile")
]