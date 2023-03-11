from rest_framework import serializers
from .models import DagPlanning, BuildingPicture, InfoPerBuilding, WeekPlanning


class DagPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = DagPlanning
        fields = [
            "student",
            "date",
            "ronde",
            "info"
        ]

    def create(self, validated_data):
        date = validated_data['date']
        info = validated_data['info']
        dagplanning = DagPlanning(date=date, info=info)
        dagplanning.save()
        return dagplanning


class BuildingPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingPicture
        fields = [
            "image",
            "time",
            "remark"
        ]


class InfoPerBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPerBuilding
        fields = [
            "arrival",
            "storage",
            "departure",
            "extra",
            "remark"
        ]


class WeekPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekPlanning
        fields = [
            "week",
            "year",
            "dagplanningen"
        ]
