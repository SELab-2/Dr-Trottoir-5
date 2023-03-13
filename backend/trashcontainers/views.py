from rest_framework import generics
from users.permissions import ReadOnly, AdminPermission, SuperstudentPermission
from .models import TrashContainer
from .serializers import TrashContainerSerializer


class TrashContainerListCreateView(generics.ListCreateAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
    permission_classes = [ReadOnly|AdminPermission|SuperstudentPermission]

class TrashContainerRetrieveView(generics.RetrieveAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
