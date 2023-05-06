from rest_framework import generics
from users.permissions import StudentReadOnly, AdminPermission, \
    SuperstudentPermission
from .models import PickUpDay, WeekDayEnum
from .serializers import PickUpSerializer
from exceptions.exceptionHandler import ExceptionHandler


class PickUpListCreateView(generics.ListCreateAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        data: dict
        data = request.data

        handler = ExceptionHandler()
        handler.check_enum_value_required(data.get("day"), "day",
                                          WeekDayEnum.values)
        handler.check_time_value_required(data.get("start_hour"), "start_hour")
        handler.check_time_value_required(data.get("end_hour"), "end_hour")
        handler.check()

        return super().post(request, *args, **kwargs)


class PickUpDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def put(self, request, *args, **kwargs):
        data: dict
        data = request.data

        handler = ExceptionHandler()
        handler.check_enum_value_required(data.get("day"), "day",
                                          PickUpDay.WeekDayEnum.values)
        handler.check_time_value_required(data.get("start_hour"), "start_hour")
        handler.check_time_value_required(data.get("end_hour"), "end_hour")
        handler.check()
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_enum_value(data.get("day"), "day",
                                 PickUpDay.WeekDayEnum.values)
        handler.check_time_value(data.get("start_hour"), "start_hour")
        handler.check_time_value(data.get("end_hour"), "end_hour")
        handler.check()
        return super().patch(request, *args, **kwargs)
