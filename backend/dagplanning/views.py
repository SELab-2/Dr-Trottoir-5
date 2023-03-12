from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializers import *

from rest_framework import serializers, status


# Create your views here.


class DagPlanningCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializer

    def post(self, request, *args, **kwargs):

        try:
            InfoPerBuilding.objects.get(pk=request.data["info"])
        except InfoPerBuilding.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "you shall not pass", "field": "info"
                        }
                    ]
                }
                , code='invalid')
        return super().post(request=request, args=args, kwargs=kwargs)


class DagPlanningRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializer


class BuildingPictureCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer

    def post(self, request, *args, **kwargs):
        errorList = []
        for i in ["arrival", "storage", "departure", "extra"]:
            try:
                BuildingPicture.objects.get(pk=request.data[i])
            except BuildingPicture.DoesNotExist:
                errorList.append({
                    "message": "key not in database", "field": i
                })
        if len(errorList) > 0:
            raise serializers.ValidationError({"errors": errorList})
        return super().post(request, args, kwargs)


class BuildingPictureRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer


class InfoPerBuildingCLAPIView(generics.ListCreateAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer


class InfoPerBuildingRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer


class WeekPlanningCLAPIView(generics.ListCreateAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer


class WeekPlanningRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer
