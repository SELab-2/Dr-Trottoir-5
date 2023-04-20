from rest_framework import serializers
from .models import *
from ronde.serializers import BuildingRelatedField
from trashcontainers.serializers import TrashContainerRelatedField


class TrashContainerIdWrapperSerializer(serializers.ModelSerializer):
    trash_container = TrashContainerRelatedField(read_only=True)

    class Meta:
        model = TrashContainerIdWrapper
        fields = ['trash_container', 'extra_id']


class TrashContainerIdWrapperRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return TrashContainerIdWrapperSerializer(value).data

    def to_internal_value(self, data):
        return data


class BuildingTrashContainerListSerializer(serializers.ModelSerializer):
    building = BuildingRelatedField(read_only=True)

    class Meta:
        model = BuildingTrashContainerList
        fields = ['building', 'trash_ids']


class BuildingTrashContainerListRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return BuildingTrashContainerListSerializer(value).data

    def to_internal_value(self, data):
        return data


class TrashContainerTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrashContainerTemplate
        fields = ['id', 'name', 'even', 'status', 'location', 'year', 'week']


class TrashContainerTemplateSerializerFull(serializers.ModelSerializer):
    trash_containers = TrashContainerIdWrapperRelatedField(many=True, read_only=True)
    buildings = BuildingTrashContainerListRelatedField(many=True, read_only=True)

    class Meta:
        model = TrashContainerTemplate
        fields = "__all__"
