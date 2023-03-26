from rest_framework import generics
from .serializers import *
from users.permissions import StudentReadOnly, AdminPermission, \
    SuperstudentPermission, StudentPermission
from django.contrib.auth import get_user_model
from ronde.models import Ronde
from .models import *

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
                    "message": "field is required",
                    "field": "weekPlanning"
                }
            )
        else:
            try:
                WeekPlanning.objects.get(pk=request.data["weekPlanning"])
            except (WeekPlanning.DoesNotExist, ValueError):
                errors.append({
                    "message": "referenced pk not in db",
                    "field": "weekPlanning"
                })

        if data.get("date") is None:
            errors.append({
                "message": "field is required",
                "field": "date"
            })
        else:
            try:
                datetime.datetime.strptime(data["date"], "%Y-%m-%d")
            except ValueError:
                errors.append({
                    "message": "date has the wrong format, use YYYY-MM-DD",
                    "field": "date"
                })
        if data.get("student") is None:
            errors.append({
                "message": "field is required",
                "field": "student"
            })
        else:
            try:
                get_user_model().objects.get(pk=data["student"])
            except (get_user_model().DoesNotExist, ValueError):
                errors.append({
                    "message": "referenced pk not in db",
                    "field": "student"
                })

        if data.get("ronde") is None:
            errors.append({
                "message": "field is required",
                "field": "ronde"
            })
        else:
            try:
                Ronde.objects.get(pk=data["ronde"])
            except (Ronde.DoesNotExist, ValueError):
                errors.append({
                    "message": "reference pk not in db",
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
                "message": "field is required",
                "field": "pictureType"
            })
        elif data["pictureType"] not in BuildingPicture.PictureEnum.values:
            errors.append({
                "message": "not a valid choice",
                "field": "pictureType"
            })
        if "image" not in data:
            errors.append({
                "message": "field is required",
                "field": "image"
            })
        elif data["image"] not in request.FILES.getlist("image"):
            errors.append({
                "message": "submitted data was not a file",
                "field": "image"
            })
        if "time" not in data:
            errors.append({
                "message": "field is required",
                "field": "time"
            })
        else:
            try:
                datetime.datetime.strptime(data["time"], "%Y-%m-%d %H:%M")
            except ValueError:
                errors.append({
                    "message": "time has wrong format, try YYYY-MM-DD hh:mm",
                    "field": "time"
                })
        if "infoPerBuilding" not in data:
            errors.append({
                "message": "field is required",
                "field": "infoPerBuilding"
            })
        else:
            try:
                InfoPerBuilding.objects.get(pk=request.data["infoPerBuilding"])
            except (InfoPerBuilding.DoesNotExist, ValueError):
                errors.append({
                    "message": "referenced pk not in db",
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
                "message": "field is required",
                "field": "dagPlanning"
            })
        else:
            try:
                DagPlanning.objects.get(pk=request.data["dagPlanning"])
            except (DagPlanning.DoesNotExist, ValueError):
                errors.append({
                    "message": "referenced pk not in db",
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
                "message": "field is required",
                "field": "week"
            })
        if data.get("year") is None:
            errors.append({
                "message": "field is required",
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
