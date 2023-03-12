from django.urls import path
from . import views

urlpatterns = [
    path("", views.DagPlanningCreateAndListAPIView.as_view()),
    path("<int:pk>/", views.DagPlanningRetrieveUpdateDestroyAPIView.as_view())
]
