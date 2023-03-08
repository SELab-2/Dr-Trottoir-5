from django.urls import path

from . import views

urlpatterns = [
    path('', views.WeekDaylistView.as_view()),
    path('<str:weekday>/', views.WeekDayDetailView.as_view())
]