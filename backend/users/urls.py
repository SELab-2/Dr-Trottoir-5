from django.urls import path

from .views import registration_view, role_assignment_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('group/', role_assignment_view, name='group')
]