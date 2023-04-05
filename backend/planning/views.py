from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
from users.permissions import StudentReadOnly, AdminPermission, SuperstudentPermission, StudentPermission
from ronde.models import Ronde


class DagPlanningCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        student = request.query_params['student'] if 'student' in request.query_params else None
        date = request.query_params['date'] if 'date' in request.query_params else None

        if student is not None and date is not None:
            try:
                dagPlanning = DagPlanning.objects.get(student=student, date=date)
                return Response(DagPlanningSerializerFull(dagPlanning).data)
            except DagPlanning.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "referenced pk not in db", "field": "dagPlanning"
                            }
                        ]
                    }, code='invalid')
        elif student is not None:
            try:
                dagPlanning = DagPlanning.objects.get(student=student)
                return Response(DagPlanningSerializerFull(dagPlanning).data)
            except DagPlanning.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "referenced pk not in db", "field": "dagPlanning"
                            }
                        ]
                    }, code='invalid')

        return super().get(request=request, args=args, kwargs=kwargs)

    def post(self, request, *args, **kwargs):
        try:
            WeekPlanning.objects.get(pk=request.data["weekPlanning"])
            ronde = Ronde.objects.get(pk=request.data["ronde"])
            response = super().post(request=request, args=args, kwargs=kwargs)
            dagPlanning = DagPlanning.objects.get(pk=response.data["id"])

            # Make a list of InfoPerBuilding
            for _ in ronde.buildings.all():
                InfoPerBuilding(dagPlanning=dagPlanning).save()
            return response
        except WeekPlanning.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "weekPlanning"
                        }
                    ]
                }, code='invalid')
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DagPlanningRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]


class BuildingPictureCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]
    # TODO: a user can only see the pictures that he added (?)

    def post(self, request, *args, **kwargs):
        try:
            InfoPerBuilding.objects.get(pk=request.data["infoPerBuilding"])
        except InfoPerBuilding.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "infoPerBuilding"
                        }
                    ]
                }, code='invalid')
        return super().post(request=request, args=args, kwargs=kwargs)


class BuildingPictureRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]
    # TODO: only the user that created a BuildingPicture should be able to update it


class InfoPerBuildingCLAPIView(generics.ListCreateAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]
    # TODO: a user can only see the info per building that he added (?)

    def get(self, request, *args, **kwargs):
        dagPlanning = request.query_params['dagPlanning'] if 'dagPlanning' in request.query_params else None

        if dagPlanning is not None:
            try:
                DagPlanning.objects.get(pk=dagPlanning)
                self.queryset = InfoPerBuilding.objects.filter(dagPlanning=dagPlanning)
            except Exception:
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "referenced pk not in db", "field": "dagPlanning"
                            }
                        ]
                    }, code='invalid')

        return super().get(request=request, args=args, kwargs=kwargs)

    def post(self, request, *args, **kwargs):
        try:
            DagPlanning.objects.get(pk=request.data["dagPlanning"])
        except DagPlanning.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "dagPlanning"
                        }
                    ]
                }, code='invalid')
        return super().post(request=request, args=args, kwargs=kwargs)


class InfoPerBuildingRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]
    # TODO: only the user that created an InfoPerBuilding should be able to update it


class WeekPlanningCLAPIView(generics.ListCreateAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]


class WeekPlanningRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]
