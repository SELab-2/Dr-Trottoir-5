from rest_framework import serializers
from django.db import IntegrityError

from .models import LocatieEnum, Manual, Building, Ronde


class LocatieRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return LocatieEnumSerializer(value).data

    def to_internal_value(self, data):
        return data


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


class ManualRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return ManualSerializer(value).data

    def to_internal_value(self, data):
        return data


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


class BuildingRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return BuildingSerializerFull(value).data

    def to_internal_value(self, data):
        return data


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class BuildingSerializerFull(BuildingSerializer):
    location = LocatieRelatedField(read_only=True)
    manual = ManualRelatedField(read_only=True)


class RondeRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return RondeSerializerFull(value).data

    def to_internal_value(self, data):
        return data


class RondeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ronde
        fields = '__all__'


class RondeRelatedFieldSerializer(serializers.ModelSerializer):
    location = LocatieRelatedField(read_only=True)

    class Meta:
        model = Ronde
        fields = '__all__'


class RondeSerializerFull(RondeSerializer):
    location = LocatieRelatedField(read_only=True)
    buildings = BuildingRelatedField(read_only=True, many=True)
