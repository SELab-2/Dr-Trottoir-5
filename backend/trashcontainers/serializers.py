from rest_framework import serializers
from .models import TrashContainer
from pickupdays.serializers import PickUpSerializer


class TrashContainerSerializer(serializers.ModelSerializer):

    collection_day_detail = PickUpSerializer(source='collection_day', read_only=True)

    class Meta:
        model = TrashContainer
        fields = "__all__"
