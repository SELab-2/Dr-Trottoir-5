from .models import TrashContainer
from rest_framework import serializers


class TrashContainerSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['start_hour'] > data['end_hour']:
            raise serializers.ValidationError({'start_hour': 'Start hour should not be later than end hour'})
        return data

    class Meta:
        model = TrashContainer
        fields = ['id', 'type', 'collection_days', 'special_actions', 'start_hour', 'end_hour']
