from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import os
from django.conf import settings

from .models import LocatieEnum, Manual, Building, Ronde
from .serializers import LocatieEnumSerializer, ManaulSerializer, BuildingSerializer, RondeSerializer


class LocatieEnumListCreateView(generics.ListCreateAPIView):
    queryset = LocatieEnum.objects.all()
    serializer_class = LocatieEnumSerializer

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


class ManualRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = ManaulSerializer
    """
        View that deletes and gets a specific Location
    """

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


class RondeListCreateView(generics.ListCreateAPIView):
    queryset = Ronde.objects.all()
    serializer_class = RondeSerializer
