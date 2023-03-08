from django.urls import path

from . import views

urlpatterns = [
    path('', views.PickUplistView.as_view()),
    path('<int:pk>/', views.PickUpDetailView.as_view())
]