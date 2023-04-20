from django.urls import path
from . import views

urlpatterns = [
    path("buildingpicture/", views.BuildingPictureCreateAndListAPIView.as_view()),
    path("buildingpicture/<int:pk>/", views.BuildingPictureRUDAPIView.as_view()),
    path("infoperbuilding/", views.InfoPerBuildingCLAPIView.as_view()),
    path("infoperbuilding/<int:pk>/", views.InfoPerBuildingRUDAPIView.as_view()),
    path("weekplanning/<int:year>/<int:week>/", views.week_planning_view),
    path("studenttemplates/rondes/<int:year>/<int:week>/<int:day>/<int:location>/", views.student_templates_rondes_view),
    path("studenttemplates/", views.student_templates_view),
    path("studenttemplates/<int:template_id>/", views.student_template_view),
    path("studenttemplates/<int:template_id>/rondes/", views.rondes_view),
    path("studenttemplates/<int:template_id>/rondes/<int:ronde_id>/", views.ronde_view),
    path("studenttemplates/<int:template_id>/rondes/<int:ronde_id>/dagplanningen/", views.dagplanningen_view),
    path("studenttemplates/<int:template_id>/dagplanningen/<int:dag_id>/", views.dagplanning_view, {'permanent': True}),
    path("studenttemplates/<int:template_id>/dagplanningen/<int:dag_id>/eenmalig/", views.dagplanning_view,
         {'permanent': False})

]
