import re

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from cart.utils import add_cart_item, add_paramters_to_url
from cart.models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def loginView(request):
    login_user = None
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('pass')
        
        if re.match(r'^\+?(?:[0-9] ?){6,14}[0-9]$', user):
            login_user = authenticate(request, mobile=user, password=password)
        elif re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', user):
            try:
                email_user = User.objects.get(email = user)
            except User.DoesNotExist:
                raise Http404
            login_user = authenticate(request, username = email_user.username, password=password)
        print("authenticated")
        if login_user is not None:
            login(request, login_user)
            # url = '/search/'
            # parsed_url = urlparse(url)
            # param = parse_qs(parsed_url.query)
            # param.update({'pid': 'w8i4o7y389'})
            # query_string = urlencode(param, doseq=True)
            # print("Query String", query_string)
            # final_url = urlunparse(parsed_url._replace(query = query_string))
            # print("final URL", final_url)
            action = request.GET.get('action')
            if action == 'add_cart_item':
                pid = request.GET.get('pid')
                sub = request.GET.get('sub')
                search = request.GET.get('search')
                next_url = request.GET.get('next', '/')
                url = add_paramters_to_url(next_url, {'search': search})
                add_cart_item(login_user, pid, sub)
                # redirect('')
                print("redirect", url)
                return redirect(url)
            # print(request.GET.get('next'))
            if request.GET.get('next') is not None:
                print(request.GET.get('next'))
                return redirect(request.GET.get('next', '/'))
            else:
                return redirect("home")
        else:
            context = {
                'error': "Invalid username or password"
            }
            return render(request, 'user/login.html', context)
    return render(request, "user/login.html", {})


def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    u_form = UserRegistrationForm()
    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST)
        if u_form.is_valid():
            instance = u_form.save(commit=False)
            instance.username = instance.first_name
            instance.save()
            profile = Profile.objects.get(user=instance)
            profile.mobile = u_form.cleaned_data.get('mobile')
            profile.save()
            print(instance)
            print("Cleaned Data",  u_form.cleaned_data)
            return redirect("user-login")
        else:
            return render(request, 'user/register.html', {'u_form': u_form})
        
    else:
        print("Get Method")
        return render(request, 'user/register.html', {'u_form': u_form})

@login_required 
def profile(request):
    orders = request.user.user_orders.all().order_by("-ordered_at")
    return render(request, 'user/profile.html', {'orders': orders})

def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'GET':
        return JsonResponse({"username": user.username, "email": user.email, 'profile': user.user_profile.profile_pic.url})
    elif request.method == 'POST':
        try:
            # Handle the errors for duplicate username and email update - Need to Update
            username = request.POST.get("username")
            email = request.POST.get("email")
            profile = request.FILES.get("profile")
            user.username = username
            user.email=email
            user.save()
            if profile:
                # Validate if the uploaded file is image or not - Need to Update
                user.user_profile.profile_pic = profile
                user.user_profile.save()
            return JsonResponse({"username": user.username, "email": user.email, 'profile': user.user_profile.profile_pic.url})
        except Exception as e:
            print("Values of Exception is : ", e)