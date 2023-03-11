from rest_framework import serializers

from .models import TrashContainer
from pickupdays.serializers import PickUpSerializer

class TrashContainerSerializer(serializers.ModelSerializer):
    collection_days_detail = PickUpSerializer(source='collection_days', many=True, read_only=True)
    class Meta:
        model = TrashContainer
        fields = ['type', 'collection_days', 'collection_days_detail', 'special_actions']

    def create(self, validated_data):
        """
            Only create a new instance if none already exists.
        """
        options = TrashContainer.objects.filter(
            type=validated_data['type'],
            special_actions=validated_data["special_actions"]
        )

        validated_data['collection_days'].sort()
        if options.exists():
            for option in options:
                collection_days = sorted(list(option.collection_days.all()))
                if validated_data['collection_days'] == collection_days:
                    return option

        return super().create(validated_data)


