from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Registration, RoleAssignment


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class RoleAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleAssignment
        fields = '__all__'


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone_nr',
            'role'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'id',
            'role'
        ]
