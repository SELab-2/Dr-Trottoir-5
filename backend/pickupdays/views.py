from rest_framework import generics

from .models import PickUpDay
from .serializers import PickUpSerializer

class PickUpListCreateView(generics.ListCreateAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer

class PickUpDetailView(generics.RetrieveAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer

