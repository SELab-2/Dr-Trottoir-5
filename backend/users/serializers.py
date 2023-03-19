from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Registration, RoleAssignment

from customserializer.CustomSerializer import CustomSerializer


class RegistrationSerializer(CustomSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

    required_fields = [
        "email",
        "first_name",
        "last_name",
        "password"
    ]


class RoleAssignmentSerializer(CustomSerializer):
    class Meta:
        model = RoleAssignment
        fields = '__all__'

    required_fields = [
        "email"
    ]

# geen custom serializer nodig
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'first_name',
            'last_name',
            'role'
        ]
