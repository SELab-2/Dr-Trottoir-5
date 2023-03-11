from django.urls import path
from . import views

urlpatterns = [
    path("", views.DagPlanningCreateAPIView.as_view())
]
