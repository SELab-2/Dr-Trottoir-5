from rest_framework import serializers
from .models import MailTemplate



class MailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = MailTemplate

