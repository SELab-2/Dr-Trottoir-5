from django.urls import path
from . import views

urlpatterns = [
    path("buildingpicture/", views.BuildingPictureCreateAndListAPIView.as_view()),
    path("buildingpicture/<int:pk>/", views.BuildingPictureRUDAPIView.as_view()),
    path("infoperbuilding/", views.InfoPerBuildingCLAPIView.as_view()),
    path("infoperbuilding/<int:pk>/", views.InfoPerBuildingRUDAPIView.as_view()),
    path("weekplanning/<int:year>/<int:week>/", views.week_planning_view),
    path("studenttemplates/", views.student_templates_view),
    path("studenttemplates/<int:template_id>/", views.student_template_view),
    path("studenttemplates/<int:template_id>/rondes/", views.rondes_view),
    path("studenttemplates/<int:template_id>/<int:ronde_id>/dagplanningen/", views.dagplanning_view)

]
