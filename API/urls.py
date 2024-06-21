from django.urls import path
from django.http import HttpResponse
from rest_framework.authtoken import views as authviews
from . import views


urlpatterns = [
    
    path('Login/',authviews.obtain_auth_token),
    path('register/',views.createuser),
]