from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializer import UserCreateSerializer

@api_view(['POST','GET'])
def createuser(request):
    if request.data :
        data  = request.data
        UserObj = User.objects.create_user(username=data['user_name'],first_name=data['first_name'],last_name=data['last_name'],email=data['email'],is_staff=data['is_staff'])
        UserObj.set_password(data['password'])
        UserObj.save()
        uObj = User.objects.get(username=data['user_name'])
        token = Token.objects.create(user=uObj)
        token.save()
        return Response( status=HTTP_201_CREATED)
    return Response(status=HTTP_400_BAD_REQUEST)

    
