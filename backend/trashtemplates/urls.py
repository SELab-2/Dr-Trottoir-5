from django.urls import path

from . import views

urlpatterns = [
    path('', views.TrashContainerTemplateListCreateView.as_view()),
    path('<int:template_id>/add/perm/', views.perm_add_trash_container),
    path('<int:template_id>/edit/temp/', views.temp_edit_trash_container)
]
