from django.urls import path

from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('role/', role_assignment_view, name='role'),
    path('users/', UserListAPIView.as_view(), name='users'),
    path('user/', UserRetrieveDestroyView.as_view(), name='user'),
    path('forgot/', forgot_password, name='forgot'),
    path('reset/', reset_password, name='reset'),
    path('logout/', TokenBlacklistView.as_view(), name='logout')
]
