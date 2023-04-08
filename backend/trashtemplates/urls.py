from django.urls import path

from . import views

urlpatterns = [
    path('', views.TrashContainerTemplateListCreateView.as_view()),
    path('<int:template_id>/add/trashcontainer/', views.add_trash_container_view),
    path('<int:template_id>/delete/trashcontainer/', views.delete_trash_container_view),
    path('<int:template_id>/edit/trashcontainer/', views.edit_trash_container_view)
]
