from rest_framework import serializers 
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email','is_staff']

'''def create(self,data):
        User.objects.get(data=)
        Token.objects.create(user=username)'''