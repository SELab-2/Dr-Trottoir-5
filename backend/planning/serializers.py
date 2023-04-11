from rest_framework import serializers
from .models import *
from ronde.serializers import RondeRelatedField


class DagPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = DagPlanning
        fields = '__all__'


class DagPlanningSerializerFull(DagPlanningSerializer):
    ronde = RondeRelatedField(read_only=True)


class StudentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTemplate
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
