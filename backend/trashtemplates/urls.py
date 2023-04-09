from django.urls import path

from . import views

urlpatterns = [
    path('', views.TrashContainerTemplateListCreateView.as_view()),
    path('<int:template_id>/trashcontainers/', views.trash_container_view),
    path('<int:template_id>/buildings/', views.building_view)
]
