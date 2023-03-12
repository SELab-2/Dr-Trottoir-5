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

    def create(self, validated_data):
        date = validated_data['date']
        # student = validated_data['student']
        # ronde = validated_data['ronde']
        weekplanning = validated_data["weekPlanning"]
        dagplanning = DagPlanning(
            date=date,
            weekPlanning=weekplanning,
            # ronde=ronde,
            # student=student
        )
        dagplanning.save()
        return dagplanning


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

    def create(self, validated_data):
        pictureType = validated_data["pictureType"]
        image = validated_data["image"]
        time = validated_data['time']
        remark = validated_data['remark']
        infoPerBuilding = validated_data["infoPerBuilding"]
        buildingPicture = BuildingPicture(pictureType=pictureType, image=image, time=time, remark=remark,
                                          infoPerBuilding=infoPerBuilding)
        buildingPicture.save()
        return buildingPicture


class InfoPerBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPerBuilding
        fields = [
            "remark",
            "dagPlanning",
            "pk"
        ]

    def create(self, validated_data):
        dagPlanning = validated_data["dagPlanning"]
        remark = validated_data["remark"]
        infoPerBuilding = InfoPerBuilding(dagPlanning=dagPlanning, remark=remark)
        infoPerBuilding.save()
        return infoPerBuilding


class WeekPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekPlanning
        fields = [
            "week",
            "year",
            "pk"
        ]

    def create(self, validated_data):
        week = validated_data['week']
        year = validated_data['year']
        weekPlanning = WeekPlanning(week=week, year=year)
        weekPlanning.save()
        return weekPlanning
