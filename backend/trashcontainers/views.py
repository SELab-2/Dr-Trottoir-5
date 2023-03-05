from rest_framework import generics

from .models import TrashContainer
from .serializers import TrashContainerSerializer


class TrashContainerDetailAPIView(generics.RetrieveAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer

class TrashContainerCreateAPIView(generics.CreateAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer

