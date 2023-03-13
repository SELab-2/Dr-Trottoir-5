from django.urls import path

from .views import registration_view, role_assignment_view, UserListAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('role/', role_assignment_view, name='role'),
    path('users/', UserListAPIView.as_view(), name='users')
]
