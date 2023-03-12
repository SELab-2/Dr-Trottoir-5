from rest_framework import generics, status
from rest_framework.response import Response

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
            return Response({"succes": serializer.data})
        elif "name" not in request.data:
            return Response({"error": ["Er is geen veld 'name' meegegeven"]}, status=status.HTTP_400_BAD_REQUEST)
        elif request.data["name"] == "":
            return Response({"error": "Het veld 'name' is leeg"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors)


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


class BuildingListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class RondeListCreateView(generics.ListCreateAPIView):
    queryset = Ronde.objects.all()
    serializer_class = RondeSerializer
