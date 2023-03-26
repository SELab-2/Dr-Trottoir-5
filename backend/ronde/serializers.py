from rest_framework import serializers
from django.db import IntegrityError

from .models import LocatieEnum, Manual, Building, Ronde


class LocatieEnumSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocatieEnum
        fields = '__all__'

    def create(self, validated_data):
        """
            Created a location record in the database or gives an already existing one
        """
        try:
            location, _ = LocatieEnum.objects.get_or_create(
                name=validated_data["name"]
            )
            return location
        except IntegrityError as e:
            raise serializers.ValidationError({"errors": str(e)})


class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = '__all__'

    def create(self, validated_data):
        try:
            manual, _ = Manual.objects.get_or_create(
                file=validated_data["file"],
                fileType=validated_data['fileType'],
                manualStatus=validated_data['manualStatus']
            )
            return manual
        except IntegrityError as e:
            raise serializers.ValidationError({"errors": str(e)})


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class RondeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ronde
        fields = '__all__'
