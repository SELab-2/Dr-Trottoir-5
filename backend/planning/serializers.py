from rest_framework import serializers
from .models import DagPlanning, BuildingPicture, InfoPerBuilding, WeekPlanning


class DagPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = DagPlanning
        fields = [
            "student",
            "date",
            "ronde",
            "weekPlanning",
            "pk"
        ]


class BuildingPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingPicture
        fields = [
            "pictureType",
            "image",
            "time",
            "remark",
            "infoPerBuilding",
            "pk"
        ]


class InfoPerBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPerBuilding
        fields = [
            "remark",
            "dagPlanning",
            "pk"
        ]


class WeekPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekPlanning
        fields = [
            "week",
            "year",
            "pk"
        ]
