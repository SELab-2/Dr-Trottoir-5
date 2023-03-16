from rest_framework import generics
from .models import MailTemplate
from .serializers import MailTemplateSerializer
from users.permissions import AdminPermission, SuperstudentPermission


class MailTemplateCreateAndListView(generics.ListCreateAPIView):
    queryset = MailTemplate.objects.all()
    serializer_class = MailTemplateSerializer
    permission_classes = [AdminPermission | SuperstudentPermission]


class MailTemplateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MailTemplate.objects.all()
    serializer_class = MailTemplateSerializer
    permission_classes = [AdminPermission | SuperstudentPermission]
