from rest_framework import generics

from .models import TrashContainer
from .serializers import TrashContainerSerializer


class TrashContainerListCreateView(generics.ListCreateAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer

class TrashContainerRetrieveView(generics.RetrieveAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer

