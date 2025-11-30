from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import RegexValidator

from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    mobile_validator = RegexValidator(
        regex = r'^\+?(?:[0-9] ?){6,14}[0-9]$',
        message= 'Enter valid mobile number',
    )

    email_validator = RegexValidator(
        regex= r'^[\w\.-]+@[\w\.-]+\.\w+$',
        message= "Enter a valid email"
    )

    mobile = forms.CharField(label="Phone", validators = [mobile_validator])
    email = forms.EmailField(validators= [email_validator])
    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1', 'password2']
        widgets = {
            'mobile' : forms.TextInput(attrs = {'class': 'NewClass'}),
            'password1': forms.PasswordInput(attrs={'class': 'PasswordField'})
        }