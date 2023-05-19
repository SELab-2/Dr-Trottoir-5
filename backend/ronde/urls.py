from django.urls import path

from . import views

urlpatterns = [
    path('', views.RondeListCreateView.as_view()),
    path('<int:pk>/', views.RondeRetrieveDestroyView.as_view()),
    path('locatie/', views.LocatieEnumListCreateView.as_view()),
    path('locatie/<int:pk>/', views.LocatieEnumRetrieveDestroyView.as_view()),
    path('building/manual/', views.ManualListCreateView.as_view()),
    path('building/manual/<int:pk>/', views.ManualRetrieveUpdateDestroyAPIView.as_view()),
    path('building/', views.BuildingListCreateView.as_view()),
    path('building/<int:pk>/', views.BuildingRetrieveDestroyView.as_view()),
    path('building/uuid/<uuid:buildingid>/',
         views.BuildingUUIDRetrieveView.as_view()),
    path('building/uuid/<uuid:buildingid>/reset/',
         views.BuildingUUIDResetView.as_view())

]
