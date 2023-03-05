from rest_framework import serializers

from .models import TrashContainer

class TrashContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashContainer
        fields = [
            "type",
            "collection_days",
            "special_actions",
            "start_hour",
            "end_hour"
        ]