from django.urls import path

from . import views

urlpatterns = [
    path('locatie/', views.LocatieEnumListCreateView.as_view(), name="location")
]
