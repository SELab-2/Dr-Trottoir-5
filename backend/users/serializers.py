from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import RoleAssignment


class RoleAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleAssignment
        fields = '__all__'


class UserRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return UserPublicSerializer(value).data

    def to_internal_value(self, data):
        return data


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone_nr',
            'role',
            'locations'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'phone_nr',
            'id',
            'role',
            'locations'
        ]
