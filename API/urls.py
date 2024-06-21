from django.urls import path
from rest_framework.authtoken import views as authviews
from . import views



urlpatterns = [
    
    path('Login/',authviews.obtain_auth_token),
    path('register/',views.createuser),
    path('Logout/',views.logout_view),
    
]