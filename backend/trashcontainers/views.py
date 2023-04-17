from rest_framework import generics
from users.permissions import StudentReadOnly, AdminPermission, \
    SuperstudentPermission
from .serializers import *
from .serializers import TrashContainerSerializer
from exceptions.exceptionHandler import ExceptionHandler
from pickupdays.models import PickUpDay
from ronde.models import Building


class TrashContainerListCreateView(generics.ListCreateAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_enum_value_required(data.get("type"), "type",
                                          TrashContainer.TrashType.values)
        handler.check_primary_key_value_required(data.get("collection_days"),
                                                 "collection_days",
                                                 PickUpDay)
        handler.check_primary_key_value_required(data.get("building"),
                                                 "building", Building)
        handler.check()
        return super().post(request, *args, **kwargs)


class TrashContainerRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def put(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_enum_value_required(data.get("type"), "type",
                                          TrashContainer.TrashType.values)
        handler.check_primary_key_value_required(data.get("collection_days"),
                                                 "collection_days",
                                                 PickUpDay)
        handler.check_primary_key_value_required(data.get("building"),
                                                 "building", Building)
        handler.check()
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_enum_value(data.get("type"), "type",
                                 TrashContainer.TrashType.values)
        handler.check_primary_key(data.get("collection_days"),
                                  "collection_days", PickUpDay)
        handler.check_primary_key(data.get("building"), "building", Building)
        handler.check()
        return super().patch(request, *args, **kwargs)
