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
            WeekPlanning.objects.get(pk=request.data["weekPlanning"])
        except WeekPlanning.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "weekPlanning"
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
        try:
            InfoPerBuilding.objects.get(pk=request.data["infoPerBuilding"])
        except InfoPerBuilding.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "infoPerBuilding"
                        }
                    ]
                }
                , code='invalid')
        return super().post(request=request, args=args, kwargs=kwargs)




class BuildingPictureRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer


class InfoPerBuildingCLAPIView(generics.ListCreateAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer

    def post(self, request, *args, **kwargs):
        try:
            DagPlanning.objects.get(pk=request.data["dagPlanning"])
        except DagPlanning.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "dagPlanning"
                        }
                    ]
                }
                , code='invalid')
        return super().post(request=request, args=args, kwargs=kwargs)


class InfoPerBuildingRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer


class WeekPlanningCLAPIView(generics.ListCreateAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer


class WeekPlanningRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer
