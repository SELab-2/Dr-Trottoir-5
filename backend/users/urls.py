from django.urls import path

from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('role/', role_assignment_view, name='role'),
    path('users/', UserListAPIView.as_view(), name='users'),
    path('forgot/', forgot_password, name='forgot'),
    path('reset/', reset_password, name='reset'),
    path('logout/', logout_view, name='logout')
]
