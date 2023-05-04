from rest_framework import serializers

from .models import PickUpDay


class PickUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUpDay
        fields = ['day', 'start_hour', 'end_hour']

    def create(self, validated_data):
        pickup, _ = PickUpDay.objects.get_or_create(**validated_data)
        return pickup

    def validate(self, data):
        if data.get('start_hour', 0) > data.get('end_hour', 0):
            raise serializers.ValidationError({'start_hour': 'Starttijd mag niet later zijn dan eindtijd'})
        return data


class PickUpDayRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return PickUpSerializer(value).data

    def to_internal_value(self, data):
        return data
