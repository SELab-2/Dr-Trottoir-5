from django.urls import path

from . import views

urlpatterns = [
    path('', views.trash_templates_view),
    path('<int:template_id>/', views.trash_template_view),
    path('<int:template_id>/trashcontainers/', views.trash_containers_view, {'permanent': True}),
    path('<int:template_id>/trashcontainers/eenmalig/', views.trash_containers_view, {'permanent': False}),
    path('<int:template_id>/trashcontainers/<int:extra_id>/', views.trash_container_view, {'permanent': True}),
    path('<int:template_id>/trashcontainers/<int:extra_id>/eenmalig/', views.trash_container_view, {'permanent': False}),
    path('<int:template_id>/buildings/', views.buildings_view, {'permanent': True}),
    path('<int:template_id>/buildings/eenmalig/', views.buildings_view, {'permanent': False}),
    path('<int:template_id>/buildings/<int:building_id>/', views.building_view, {'permanent': True}),
    path('<int:template_id>/buildings/<int:building_id>/eenmalig/', views.building_view, {'permanent': False})
]
