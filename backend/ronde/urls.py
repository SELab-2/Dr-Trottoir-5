from django.urls import path

from . import views

urlpatterns = [
    path('', views.LocatieEnumListCreateView.as_view(), name="location")
]
