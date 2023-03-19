from rest_framework import serializers
from .models import MailTemplate

from customserializer.CustomSerializer import CustomSerializer


class MailTemplateSerializer(CustomSerializer):
    class Meta:
        fields = "__all__"
        model = MailTemplate

    required_fields = ["name", "content"]
