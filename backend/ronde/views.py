from .models import *
from .serializers import *

from exceptions.exceptionHandler import ExceptionHandler
import os

from django.conf import settings
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from users.permissions import StudentReadOnly, AdminPermission, \
    SuperstudentPermission, SyndicusPermission


class LocatieEnumListCreateView(generics.ListCreateAPIView):
    queryset = LocatieEnum.objects.all()
    serializer_class = LocatieEnumSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank_required(data.get("name"), "name")
        handler.check()
        return super().post(request, *args, **kwargs)


class LocatieEnumRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocatieEnumSerializer
    queryset = LocatieEnum.objects.all()
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]
    """
        View that deletes and gets a specific Location
    """

    def put(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank_required(data.get("name"), "name")
        handler.check()
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank(data.get("name"), "name")
        handler.check()
        return super().patch(request, *args, **kwargs)


class ManualListCreateView(generics.ListCreateAPIView):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        data: dict = request.data
        handler = ExceptionHandler()
        handler.check_file_required(data.get("file"), "file", request.FILES)
        handler.check_not_blank_required(data.get("fileType"), "fileType")
        handler.check_enum_value_required(data.get("manualStatus"),
                                          "manualStatus",
                                          ManualStatusField.values)
        handler.check()
        return super().post(request, *args, **kwargs)


class ManualRetrieveUpdateDestroyAPIView(
        generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManualSerializer
    queryset = Manual.objects.all()
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]
    """
        View that gets, deletes and updates a specific Manual
    """

    def delete(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        manual = Manual.objects.filter(id=id)
        if len(manual) == 0:
            return Response({"error": [f"Manual met {id} is niet aanwezig"]},
                            status=status.HTTP_400_BAD_REQUEST)
        for man in manual:
            os.remove(os.path.join(settings.MEDIA_ROOT, man.file.name))
            man.delete()
        return Response({"succes": ["Manual is verwijdert"]},
                        status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data: dict = request.data
        handler = ExceptionHandler()
        handler.check_file_required(data.get("file"), "file", request.FILES)
        handler.check_not_blank_required(data.get("fileType"), "fileType")
        handler.check_enum_value_required(data.get("manualStatus"),
                                          "manualStatus",
                                          ManualStatusField.values)
        handler.check()
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_file(data.get("file"), "file", request.FILES)
        handler.check_not_blank(data.get("fileType"), "fileType")
        handler.check_enum_value(data.get("manualStatus"), "manualStatus",
                                 ManualStatusField.values)
        return super().patch(request, *args, **kwargs)


class BuildingListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank_required(data.get("name"), "name")
        handler.check_not_blank_required(data.get("adres"), "adres")
        handler.check_integer_required(data.get("ivago_klantnr"),
                                       "ivago_klantnr")
        handler.check_primary_key_value_required(data.get("manual"), "manual",
                                                 Manual)
        handler.check_primary_key_value_required(data.get("location"),
                                                 "location", LocatieEnum)
        handler.check()
        return super().post(request, *args, **kwargs)


class BuildingRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildingSerializerFull
    queryset = Building.objects.all()
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def put(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank_required(data.get("adres"), "adres")
        handler.check_integer_required(data.get("ivago_klantnr"),
                                       "ivago_klantnr")
        handler.check_primary_key_value_required(data.get("manual"), "manual",
                                                 Manual)
        handler.check_primary_key_value_required(data.get("location"),
                                                 "location", LocatieEnum)
        handler.check()
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank(data.get("adres"), "adres")
        handler.check_not_blank(data.get("name"), "name")
        handler.check_integer(data.get("ivago_klantnr"), "ivago_klantnr")
        handler.check_primary_key(data.get("manual"), "manual", Manual)
        handler.check_primary_key(data.get("location"), "location",
                                  LocatieEnum)
        handler.check()
        return super().patch(request, *args, **kwargs)


class BuildingUUIDRetrieveView(generics.RetrieveAPIView):
    serializer_class = BuildingSerializerFull

    def get(self, request, *args, **kwargs):
        id = kwargs["buildingid"]
        buildings = Building.objects.filter(buildingID=id)
        if buildings.exists():
            serializer = self.get_serializer(buildings.get())
            return Response(serializer.data)
        return Response(status=404)


class BuildingUUIDResetView(generics.RetrieveAPIView):
    permission_classes = \
        [SyndicusPermission | AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        id = kwargs["buildingid"]
        buildings = Building.objects.filter(buildingID=id)
        if buildings.exists():
            building = buildings.get()
            building.buildingID = uuid.uuid4()
            building.save()
            return Response({"message": "success"})
        return Response(status=404)


class RondeListCreateView(generics.ListCreateAPIView):
    queryset = Ronde.objects.all()
    serializer_class = RondeSerializer
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def post(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank_required(data.get("name"), "name")
        handler.check_primary_key_value_required(data.get("location"),
                                                 "location", LocatieEnum)
        # TODO fix building list check ook put en patch
        handler.check()
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RondeRelatedFieldSerializer
        else:
            return RondeSerializer


class RondeRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RondeSerializer
    queryset = Ronde.objects.all()
    permission_classes = [
        StudentReadOnly | AdminPermission | SuperstudentPermission]

    def put(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank_required(data.get("name"), "name")
        handler.check_primary_key_value_required(data.get("location"),
                                                 "location", LocatieEnum)
        # handler.check_primary_key_value_required(data.get("buildings"),
        # "buildings", Building)
        handler.check()
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank("name")
        handler.check_primary_key(data.get("location"), "location",
                                  LocatieEnum)
        # handler.check_primary_key(data.get("buildings"), "buildings",
        # Building)
        handler.check()
        return super().put(request, *args, **kwargs)
