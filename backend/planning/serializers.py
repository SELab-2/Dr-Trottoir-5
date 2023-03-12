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

    def create(self, validated_data):
        image = validated_data["image"]
        info = validated_data['info']
        remark = validated_data['remark']
        buildingPicture = BuildingPicture(image=image, info=info, remark=remark)
        buildingPicture.save()
        return buildingPicture


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

    def create(self, validated_data):
        arrival = validated_data['arrival']
        storage = validated_data['storage']
        departure = validated_data['departure']
        extra = validated_data['extra']
        remark = validated_data[remark]
        infoPerBuilding = InfoPerBuilding(arrival=arrival, storage=storage, departure=departure, extra=extra,
                                          remark=remark)
        infoPerBuilding.save()
        return infoPerBuilding


class WeekPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekPlanning
        fields = [
            "week",
            "year",
            "dagplanningen"
        ]

    def create(self, validated_data):
        week = validated_data['week']
        year = validated_data['year']
        dagplanning = validated_data['dagplanningen']
        weekPlanning = WeekPlanning(week=week, year=year, dagplanning=dagplanning)
        weekPlanning.save()
        return weekPlanning
