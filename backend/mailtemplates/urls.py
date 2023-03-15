
from django.urls import path
from . import views
urlpatterns = [
    path("", views.MailTemplateCreateAndListView.as_view()),
    path("<int:pk>/", views.MailTemplateRetrieveUpdateDestroyAPIView.as_view())
]