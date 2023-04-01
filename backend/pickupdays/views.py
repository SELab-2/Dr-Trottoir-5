from rest_framework import generics, serializers
from users.permissions import StudentReadOnly, AdminPermission, \
    SuperstudentPermission
from .models import PickUpDay
from .serializers import PickUpSerializer
from exceptions.exceptionHandler import ExceptionHandler


class PickUpListCreateView(generics.ListCreateAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        errors = []
        data: dict
        data = request.data

        handler = ExceptionHandler()
        handler.checkEnumValue(data.get("day"), "day",
                               PickUpDay.WeekDayEnum.values)
        handler.checkTimeValue(data.get("start_hour"), "start_hour")
        handler.checkTimeValue(data.get("end_hour"), "end_hour")
        handler.check()

        return super().post(request, *args, **kwargs)


class PickUpDetailView(generics.RetrieveAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]
