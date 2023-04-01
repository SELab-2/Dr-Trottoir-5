from rest_framework import generics
from .serializers import *
from users.permissions import StudentReadOnly, AdminPermission, \
    SuperstudentPermission, StudentPermission
from django.contrib.auth import get_user_model
from ronde.models import Ronde
from .models import *
from exceptions.exceptionHandler import ExceptionHandler
import datetime


class DagPlanningCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        data = request.data
        errors = []
        if data.get("weekPlanning") is None:
            errors.append(
                {
                    "message": ExceptionMessage.required_error,
                    "field": "weekPlanning"
                }
            )
        else:
            try:
                WeekPlanning.objects.get(pk=request.data["weekPlanning"])
            except (WeekPlanning.DoesNotExist, ValueError):
                errors.append({
                    "message": ExceptionMessage.pk_does_not_exist_error,
                    "field": "weekPlanning"
                })

        if data.get("date") is None:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "date"
            })
        else:
            try:
                datetime.datetime.strptime(data["date"], "%Y-%m-%d")
            except ValueError:
                errors.append({
                    "message": ExceptionMessage.date_format_error,
                    "field": "date"
                })
        if data.get("student") is None:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "student"
            })
        else:
            try:
                get_user_model().objects.get(pk=data["student"])
            except (get_user_model().DoesNotExist, ValueError):
                errors.append({
                    "message": ExceptionMessage.pk_does_not_exist_error,
                    "field": "student"
                })

        if data.get("ronde") is None:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "ronde"
            })
        else:
            try:
                Ronde.objects.get(pk=data["ronde"])
            except (Ronde.DoesNotExist, ValueError):
                errors.append({
                    "message": ExceptionMessage.pk_does_not_exist_error,
                    "field": "ronde"
                })

        if len(errors) > 0:
            raise serializers.ValidationError({
                "errors": errors
            })
        return super().post(request=request, args=args, kwargs=kwargs)


class DagPlanningRetrieveUpdateDestroyAPIView(
        generics.RetrieveUpdateDestroyAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]


class BuildingPictureCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer
    permission_classes = [
        StudentPermission | AdminPermission | SuperstudentPermission]

    # TODO: a user can only see the pictures that he added (?)

    def post(self, request, *args, **kwargs):
        data = request.data
        errors = []

        if "pictureType" not in data:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "pictureType"
            })
        elif data["pictureType"] not in BuildingPicture.PictureEnum.values:
            errors.append({
                "message": ExceptionMessage.invalid_enum_choice_error,
                "field": "pictureType"
            })
        if "image" not in data:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "image"
            })
        elif data["image"] not in request.FILES.getlist("image"):
            errors.append({
                "message": ExceptionMessage.file_upload_error,
                "field": "image"
            })
        if "time" not in data:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "time"
            })
        else:
            try:
                datetime.datetime.strptime(data["time"], "%Y-%m-%d %H:%M")
            except ValueError:
                errors.append({
                    "message": ExceptionMessage.datetime_format_error,
                    "field": "time"
                })
        if "infoPerBuilding" not in data:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "infoPerBuilding"
            })
        else:
            try:
                InfoPerBuilding.objects.get(pk=request.data["infoPerBuilding"])
            except (InfoPerBuilding.DoesNotExist, ValueError):
                errors.append({
                    "message": ExceptionMessage.pk_does_not_exist_error,
                    "field": "infoPerBuilding"
                })
        if len(errors) > 0:
            raise serializers.ValidationError({
                "errors": errors
            })
        return super().post(request=request, args=args, kwargs=kwargs)


class BuildingPictureRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer
    permission_classes = [
        StudentPermission | AdminPermission | SuperstudentPermission]
    # TODO: only the user that created a BuildingPicture should be able to update it


class InfoPerBuildingCLAPIView(generics.ListCreateAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer
    permission_classes = [
        StudentPermission | AdminPermission | SuperstudentPermission]

    # TODO: a user can only see the info per building that he added (?)

    def post(self, request, *args, **kwargs):
        data = request.data
        errors = []
        if "dagPlanning" not in data:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "dagPlanning"
            })
        else:
            try:
                DagPlanning.objects.get(pk=request.data["dagPlanning"])
            except (DagPlanning.DoesNotExist, ValueError):
                errors.append({
                    "message": ExceptionMessage.pk_does_not_exist_error,
                    "field": "dagPlanning"
                })
        if len(errors) > 0:
            raise serializers.ValidationError({
                "errors": errors
            })
        return super().post(request=request, args=args, kwargs=kwargs)


class InfoPerBuildingRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer
    permission_classes = [
        StudentPermission | AdminPermission | SuperstudentPermission]
    # TODO: only the user that created an InfoPerBuilding should be able to update it


class WeekPlanningCLAPIView(generics.ListCreateAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):

        data = request.data
        errors = []
        if data.get("week") is None:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "week"
            })
        if data.get("year") is None:
            errors.append({
                "message": ExceptionMessage.required_error,
                "field": "year"
            })
        if len(errors) > 0:
            raise serializers.ValidationError({
                "errors": errors
            })
        return super().post(request, *args, **kwargs)


class WeekPlanningRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]
