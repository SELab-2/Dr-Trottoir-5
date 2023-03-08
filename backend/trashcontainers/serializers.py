from rest_framework import serializers

from .models import TrashContainer

class TrashContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashContainer
        fields = '__all__'