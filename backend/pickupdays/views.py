from rest_framework import generics, serializers
from users.permissions import StudentReadOnly, AdminPermission, \
    SuperstudentPermission
from .models import PickUpDay
from .serializers import PickUpSerializer
from exceptions.exceptionMessage import ExceptionMessage


class PickUpListCreateView(generics.ListCreateAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        errors = []
        data = request.data
        if data.get("day") is None:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "day"
            })
        else:
            if data["day"] not in PickUpDay.WeekDayEnum.values:
                errors.append({
                    "message": ExceptionMessage.invalid_enum_choice_error,
                    "field": "day"
                })
        if data.get("start_hour") is None:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "start_hour"
            })
        if data.get("end_hour") is None:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "end_hour"
            })
        if len(errors) > 0:
            raise serializers.ValidationError({
                "errors": errors
            })

        return super().post(request, *args, **kwargs)


class PickUpDetailView(generics.RetrieveAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]
