from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserCreateSerializer
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from django.contrib.auth import user_logged_out

@api_view(['POST'])
def createuser(request):
    UserObject = UserCreateSerializer(data=request.data)
    if UserObject.is_valid():
        UserObject.create_user(request.data['data'])
        return Response( status=HTTP_201_CREATED)
    return Response(status=HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def logout_view(request):
    user_logged_out(request)
