from django.urls import path
from . import views

urlpatterns = [
    path("buildingpicture/", views.BuildingPictureCreateAndListAPIView.as_view()),
    path("buildingpicture/<int:pk>/", views.BuildingPictureRUDAPIView.as_view()),

    path("infoperbuilding/", views.InfoPerBuildingCLAPIView.as_view()),
    path("infoperbuilding/<int:pk>/", views.InfoPerBuildingRUDAPIView.as_view()),

    path("weekplanning/<int:year>/<int:week>/", views.WeekplanningView.as_view()),

    path("dagplanning/<int:year>/<int:week>/<int:day>/",
         views.StudentDayPlan.as_view()),
    path("dagplanning/<int:pk>/", views.DagPlanningRetrieveUpdateAPIView.as_view()),

    path("studenttemplates/rondes/<int:year>/<int:week>/<int:day>/<int"
         ":location>/", views.StudentTemplateRondeView.as_view()),
    path("studenttemplates/", views.StudentTemplateView.as_view()),
    path("studenttemplates/<int:template_id>/", views.StudentTemplateDetailView.as_view()),
    path("studenttemplates/<int:template_id>/rondes/", views.RondesView.as_view()),
    path("studenttemplates/<int:template_id>/rondes/<int:ronde_id>/",
         views.RondeView.as_view()),
    path("studenttemplates/<int:template_id>/rondes/<int:ronde_id"
         ">/dagplanningen/", views.DagPlanningenView.as_view()),
    path("studenttemplates/<int:template_id>/dagplanningen/<int:dag_id>/",
         views.DagPlanningView.as_view(), {'permanent': True}),
    path("studenttemplates/<int:template_id>/dagplanningen/<int:dag_id"
         ">/eenmalig/", views.DagPlanningView.as_view(),
         {'permanent': False})
]
