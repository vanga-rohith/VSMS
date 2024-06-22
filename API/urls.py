from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import createuser


urlpatterns = [
    
    path('Login/',obtain_auth_token),
    path('register/',createuser),
    
]