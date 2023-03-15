from django.shortcuts import render
from rest_framework import generics
from .models import MailTemplate
from .serializers import MailTemplateSerializer


# Create your views here.

class MailTemplateCreateAndListView(generics.ListCreateAPIView):
    queryset = MailTemplate.objects.all()
    serializer_class = MailTemplateSerializer


class MailTemplateRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView):
    queryset = MailTemplate.objects.all()
    serializer_class = MailTemplateSerializer
