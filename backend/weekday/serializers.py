from rest_framework import serializers

from .models import Weekday

class WeekdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekday
        fields = '__all__'