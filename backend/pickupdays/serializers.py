from rest_framework import serializers

from .models import PickUpDay

class  PickUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUpDay
        fields = '__all__'