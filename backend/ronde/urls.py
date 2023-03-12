from django.urls import path

from . import views

urlpatterns = [
    path('locatie/', views.LocatieEnumListCreateView.as_view()),
    path('locatie/<int:pk>/', views.LocatieEnumRetrieveDestroyView.as_view()),
    path('building/manual/', views.ManualListCreateView.as_view()),
    path('building/manual/<int:pk>', views.ManualRetrieveDestroyView.as_view())
]
