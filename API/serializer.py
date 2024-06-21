from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserCreateSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email','is_staff']

    def create_user(self,user_data):
        UserObj = User.objects.create(username=user_data['user_name'],first_name=user_data['first_name'],last_name=user_data['last_name'],email=user_data['email'],is_staff=user_data['is_staff'])
        UserObj.set_password(user_data['password'])
        UserObj.save()
        uObj = User.objects.get(username=user_data['user_name'])
        token = Token.objects.create(user=uObj)
        token.save()
        
