from rest_framework import serializers

from .models import PickUpDay

class  PickUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUpDay
        fields = '__all__'

    def create(self, validated_data):
        pickup, _ = PickUpDay.objects.get_or_create(**validated_data)
        return pickup