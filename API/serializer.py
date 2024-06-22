from rest_framework import serializers
from django.contrib.auth.models import User



class UserCreateSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email','is_staff']
        
