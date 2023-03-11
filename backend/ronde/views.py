from rest_framework import generics, status
from rest_framework.response import Response

from .models import LocatieEnum, Manual, Building, Ronde
from .serializers import LocatieEnumSerializer, ManaulSerializer, BuildingSerializer, RondeSerializer


class LocatieEnumListCreateView(generics.ListCreateAPIView):
    queryset = LocatieEnum.objects.all()
    serializer_class = LocatieEnumSerializer

    # permission_classes = (AllowAny,)  # TODO change permissions

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_402_PAYMENT_REQUIRED
                            )
        else:
            return Response(serializer.error,
                            status=status.HTTP_402_PAYMENT_REQUIRED
                            )


class ManualListCreateView(generics.ListCreateAPIView):
    queryset = Manual.objects.all()
    serializer_class = ManaulSerializer
    # permission_classes = (AllowAny,)  # TODO


class BuildingListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class RondeListCreateView(generics.ListCreateAPIView):
    queryset = Ronde.objects.all()
    serializer_class = RondeSerializer
