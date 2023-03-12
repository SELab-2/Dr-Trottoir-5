from django.urls import path
from . import views

urlpatterns = [
    path("dagplanning/", views.DagPlanningCreateAndListAPIView.as_view()),
    path("dagplanning/<int:pk>/", views.DagPlanningRetrieveUpdateDestroyAPIView.as_view()),
    path("buildingpicture/", views.BuildingPictureCreateAndListAPIView.as_view()),
    path("buildingpicture/<int:pk>/", views.BuildingPictureRUDAPIView.as_view()),
    path("infoperbuilding/", views.InfoPerBuildingCLAPIView.as_view()),
    path("infoperbuildign/<int:pk>/", views.InfoPerBuildingRUDAPIView.as_view()),
    path("weekplanning/", views.WeekPlanningCLAPIView.as_view()),
    path("weekplanning/<int:pk>/", views.WeekPlanningRUDAPIView.as_view())
]
