from rest_framework import generics
from users.permissions import StudentReadOnly, AdminPermission, SuperstudentPermission
from .models import TrashContainer
from .serializers import *
from ronde.models import Building


class TrashContainerListCreateView(generics.ListCreateAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        building = request.query_params['building'] if 'building' in request.query_params else None

        if building is not None:
            try:
                Building.objects.get(pk=building)
                self.queryset = TrashContainer.objects.filter(building=building)
            except Exception:
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "referenced pk not in db", "field": "building"
                            }
                        ]
                    }, code='invalid')

        return super().get(request=request, args=args, kwargs=kwargs)


class TrashContainerRetrieveView(generics.RetrieveAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]
