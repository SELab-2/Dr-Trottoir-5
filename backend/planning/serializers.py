from rest_framework import serializers
from .models import DagPlanning, BuildingPicture, InfoPerBuilding, WeekPlanning
from ronde.serializers import RondeRelatedField


class DagPlanningSerializer(serializers.ModelSerializer):
    ronde = RondeRelatedField(read_only=True)

    class Meta:
        model = DagPlanning
        fields = '__all__'


class BuildingPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingPicture
        fields = "__all__"


class InfoPerBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPerBuilding
        fields = "__all__"


class WeekPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekPlanning
        fields = "__all__"
