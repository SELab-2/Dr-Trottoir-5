from django.shortcuts import render
from rest_framework import generics

from .models import DagPlanning, InfoPerBuilding
from .serializers import DagPlanningSerializer

from rest_framework import serializers


# Create your views here.


class DagPlanningCreateAPIView(generics.ListCreateAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializer

    def post(self, request, *args, **kwargs):

        try:
            InfoPerBuilding.objects.get(pk=request.data["info"])
        except InfoPerBuilding.DoesNotExist:
            raise serializers.ValidationError("you shall not pass", code='invalid')
        return super().post(request=request, args=args, kwargs=kwargs)
