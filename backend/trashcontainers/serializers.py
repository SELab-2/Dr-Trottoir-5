from rest_framework import serializers
from .models import TrashContainer
from pickupdays.serializers import PickUpDayRelatedField


class TrashContainerSerializer(serializers.ModelSerializer):

    collection_day = PickUpDayRelatedField(read_only=True)

    class Meta:
        model = TrashContainer
        fields = ['collection_day', 'type']

    def create(self, validated_data):
        """
            Only create a new instance if none already exists.
        """
        options = TrashContainer.objects.filter(
            type=validated_data['type'],
            building=validated_data['building'],
            special_actions=validated_data.get("special_actions", "")
        )

        validated_data['collection_days'].sort(key=lambda x: x.day)
        if options.exists():
            for option in options:
                collection_days = sorted(list(option.collection_days.all()), key=lambda x: x.day)
                if validated_data['collection_days'] == collection_days:
                    return option


class TrashContainerRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return TrashContainerSerializer(value).data

    def to_internal_value(self, data):
        return data
