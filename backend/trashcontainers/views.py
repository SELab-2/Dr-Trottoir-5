from rest_framework import generics
from users.permissions import StudentReadOnly, AdminPermission, SuperstudentPermission
from .models import TrashContainer
from .serializers import TrashContainerSerializer


class TrashContainerListCreateView(generics.ListCreateAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]


class TrashContainerRetrieveView(generics.RetrieveAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]
