from rest_framework import generics
from users.permissions import ReadOnly, AdminPermission, SuperstudentPermission

from .models import PickUpDay
from .serializers import PickUpSerializer


class PickUpListCreateView(generics.ListCreateAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer
    permission_classes = [ReadOnly|AdminPermission|SuperstudentPermission]


class PickUpDetailView(generics.RetrieveAPIView):
    queryset = PickUpDay.objects.all()
    serializer_class = PickUpSerializer
