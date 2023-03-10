from rest_framework import generics

from .models import LocatieEnum, Manual, Building, Ronde
from .serializers import LocatieEnumSerializer, ManaulSerializer, BuildingSerializer, RondeSerializer


class LocatieEnumListCreateView(generics.ListCreateAPIView):
    queryset = LocatieEnum.objects.all()
    serializer_class = LocatieEnumSerializer

    # permission_classes = (AllowAny,)  # TODO change permissions

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": serializer.data},
                status=serializer.status
            )
        else:
            return Response(
                {"errors": serializer.errors},
                status=serializer.status
            )


class ManualListCreateView(generics.ListCreateAPIView):
    queryset = Manual.objects.all()
    serializer_class = ManaulSerializer
    # permission_classes = (AllowAny,)  # TODO
