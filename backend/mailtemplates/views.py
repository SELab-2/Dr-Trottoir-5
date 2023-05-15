from rest_framework import generics
from .models import MailTemplate
from .serializers import MailTemplateSerializer
from users.permissions import AdminPermission, SuperstudentPermission
from exceptions.exceptionHandler import ExceptionHandler


class MailTemplateCreateAndListView(generics.ListCreateAPIView):
    queryset = MailTemplate.objects.all()
    serializer_class = MailTemplateSerializer
    permission_classes = [AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank_required(data.get("name"), "name")
        handler.check_not_blank_required(data.get("content"), "content")
        handler.check()
        return super().post(request, *args, **kwargs)


class MailTemplateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MailTemplate.objects.all()
    serializer_class = MailTemplateSerializer
    permission_classes = [AdminPermission | SuperstudentPermission]

    def patch(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank(data.get("name"), "name")
        handler.check_not_blank(data.get("content"), "content")
        handler.check()
        return super().patch(request, *args, **kwargs)
