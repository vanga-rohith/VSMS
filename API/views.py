from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserCreateSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST

@api_view(['POST'])
def createuser(request):
    serializer = UserCreateSerializer(data=request.data)
    userObj =request.data['username']
    #print(userObj)
    #print(request.data['username'])
    if serializer.is_valid():
        #print(serializer.is_valid())
        serializer.save()
        token = User.objects.get(username=userObj)
        id = Token.objects.create(user=token)
        id.save()
        return Response( status=HTTP_201_CREATED)
    return Response(status=HTTP_400_BAD_REQUEST)
