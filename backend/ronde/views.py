from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import os
from django.conf import settings
from .models import LocatieEnum, Manual, Building, Ronde
from .serializers import LocatieEnumSerializer, ManaulSerializer, BuildingSerializer, RondeSerializer
from users.permissions import StudentReadOnly, AdminPermission, SuperstudentPermission


class LocatieEnumListCreateView(generics.ListCreateAPIView):
    queryset = LocatieEnum.objects.all()
    serializer_class = LocatieEnumSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]

    def create(self, request, *args, **kwargs):
        """
           Post method that creates a Location record
           Returns error when there isn't a name field or the field is empty
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes": serializer.data}, status=status.HTTP_201_CREATED)
        elif "name" not in request.data:
            return Response({"error": ["Er is geen veld 'name' meegegeven"]}, status=status.HTTP_400_BAD_REQUEST)
        elif request.data["name"] == "":
            return Response({"error": "Het veld 'name' is leeg"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocatieEnumRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = LocatieEnumSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]
    """
        View that deletes and gets a specific Location
    """

    def get_queryset(self):
        id = self.kwargs['pk']
        return LocatieEnum.objects.filter(id=id)


class ManualListCreateView(generics.ListCreateAPIView):
    queryset = Manual.objects.all()
    serializer_class = ManaulSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]

    def create(self, request, *args, **kwargs):
        """
            Post method that creates a Manual record. The manaul is saved in media root
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes": serializer.data}, status=status.HTTP_201_CREATED)
        elif "file" not in request.data or "fileType" not in request.data or "manualStatus" not in request.data:
            return Response(
                {"error": ["Een van de benodigde velden: 'file', 'fileType' of 'manualStatus is niet aanwezig"]},
                status=status.HTTP_400_BAD_REQUEST)
        elif request.data["file"] == "" or request.data["fileType"] == "" or request.data["manualStatus"] == "":
            return Response(
                {"error": ["Een van de benodigde velden: 'file', 'fileType' of 'manualStatus is leeg"]},
                status=status.HTTP_400_BAD_REQUEST)
        elif request.data["manualStatus"] not in ["Klaar", "Update nodig", "Bezig", "Geüpdatet"]:
            return Response(
                {"error": [
                    "Er is een foute manual status meegegeven. Kies uit volgende opties: Klaar, Update nodig, Bezig of "
                    "Geüpdatet"]},
                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManualRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManaulSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]
    """
        View that gets, deletes and updates a specific Manual
    """

    def partial_update(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        try:
            manual = Manual.objects.get(id=id)
            serializer = ManaulSerializer(manual, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        except Manual.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced manual not in db", "field": "id"
                        }
                    ]
                }, code='invalid')

    def delete(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        manual = Manual.objects.filter(id=id)
        if len(manual) == 0:
            return Response({"error": [f"Manual met {id} is niet aanwezig"]}, status=status.HTTP_400_BAD_REQUEST)
        for man in manual:
            os.remove(os.path.join(settings.MEDIA_ROOT, man.file.name))
            man.delete()
        return Response({"succes": ["Manual is verwijdert"]}, status=status.HTTP_200_OK)

    def get_queryset(self):
        id = self.kwargs['pk']
        return Manual.objects.filter(id=id)


class BuildingListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]


class BuildingRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildingSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]

    def partial_update(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        try:
            building = Building.objects.get(id=id)
            serializer = BuildingSerializer(building, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response({"succes": ["Updated building"]})
        except Building.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced building not in db", "field": "id"
                        }
                    ]
                }, code='invalid')

    def get_queryset(self):
        id = self.kwargs['pk']
        return Building.objects.filter(id=id)


class RondeListCreateView(generics.ListCreateAPIView):
    queryset = Ronde.objects.all()
    serializer_class = RondeSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]


class RondeRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = RondeSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]

    def get_queryset(self):
        id = self.kwargs['pk']
        return Ronde.objects.filter(id=id)
