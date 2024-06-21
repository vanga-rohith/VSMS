from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import models

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','password1','password2','email','is_staff']

