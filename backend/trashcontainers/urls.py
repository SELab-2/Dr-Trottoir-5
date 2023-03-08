from django.urls import path

from . import views

urlpatterns = [
    path('', views.TrashContainerListCreateView.as_view()),
    path('<int:pk>/', views.TrashContainerRetrieveUpdateDestroyView.as_view())
]