from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>", views.TrashContainerDetailAPIView.as_view()),
    path("", views.TrashContainerCreateAPIView.as_view())
]