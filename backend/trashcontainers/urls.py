from django.urls import path
from . import views

urlpatterns = [
    path('', views.trashcontainers),
    path('<int:pk>', views.trashcontainers_pk),
]
