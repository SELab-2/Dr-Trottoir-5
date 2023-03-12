from django.urls import path

from . import views

urlpatterns = [
    path('locatie/', views.LocatieEnumListCreateView.as_view()),
    path('locatie/<int:pk>/', views.LocatieEnumRetrieveDestroyView.as_view())
]
