from rest_framework import serializers
from .models import TrashContainer
from pickupdays.serializers import PickUpDayRelatedField


class TrashContainerSerializer(serializers.ModelSerializer):

    collection_day = PickUpDayRelatedField(read_only=True)

    class Meta:
        model = TrashContainer
        fields = ['collection_day', 'type']


class TrashContainerRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return TrashContainerSerializer(value).data

    def to_internal_value(self, data):
        return data
