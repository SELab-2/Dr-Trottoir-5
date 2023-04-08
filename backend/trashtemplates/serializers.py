from rest_framework import serializers
from .models import TrashContainerTemplate, TrashContainerIdWrapper


class TrashContainerIdWrapperSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrashContainerIdWrapper
        fields = "__all__"


class TrashContainerTemplateSerializer(serializers.ModelSerializer):
    trash_containers_detail = TrashContainerIdWrapperSerializer(source='trash_containers', many=True, read_only=True)

    class Meta:
        model = TrashContainerTemplate
        fields = "__all__"
