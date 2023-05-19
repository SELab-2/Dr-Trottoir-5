from django.urls import path

from . import views

urlpatterns = [
    path('', views.TrashTemplatesView.as_view()),
    path('<int:template_id>/', views.TrashTemplateView.as_view()),
    path('<int:template_id>/trashcontainers/',
         views.TrashContainersView.as_view(), {'permanent': True}),
    path('<int:template_id>/trashcontainers/eenmalig/',
         views.TrashContainersView.as_view(), {'permanent': False}),
    path('<int:template_id>/trashcontainers/<int:extra_id>/',
         views.TrashContainerView.as_view(), {'permanent': True}),
    path('<int:template_id>/trashcontainers/<int:extra_id>/eenmalig/',
         views.TrashContainerView.as_view(), {'permanent': False}),
    path('<int:template_id>/buildings/', views.BuildingsView.as_view(),
         {'permanent': True}),
    path('<int:template_id>/buildings/eenmalig/',
         views.BuildingsView.as_view(),
         {'permanent': False}),
    path('<int:template_id>/buildings/<int:building_id>/',
         views.BuildingView.as_view(),
         {'permanent': True}),
    path('<int:template_id>/buildings/<int:building_id>/eenmalig/',
         views.BuildingView.as_view(),
         {'permanent': False}),
    path("<int:year>/<int:week>/<int:day>/",
         views.BuildingTrashPlan.as_view()),
]
