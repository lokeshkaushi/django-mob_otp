from django.contrib import admin
from django.urls import path 
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
urlpatterns = [
    path('register/', Register.as_view(), name="Register"),
    path('login/', login_view, name="login"),
    path('otp/<uid>/', otp , name='otp'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
