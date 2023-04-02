from rest_framework import generics
from users.permissions import StudentReadOnly, AdminPermission, \
    SuperstudentPermission
from .models import TrashContainer
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
        handler.checkEnumValue(data.get("type"), "type",
                               TrashContainer.TrashType.values)
        handler.checkPKValue(data.get("collection_days"), "collection_days",
                             PickUpDay)
        handler.checkPKValue(data.get("building"), "building", Building)
        handler.check()
        return super().post(request, *args, **kwargs)


class TrashContainerRetrieveView(generics.RetrieveAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]
