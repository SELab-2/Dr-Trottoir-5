from rest_framework import generics
from users.permissions import StudentReadOnly, AdminPermission, SuperstudentPermission
from .serializers import *
from ronde.models import Building
from rest_framework.response import Response
from planning.models import WeekPlanning
from trashtemplates.models import TrashContainerIdWrapper


class TrashContainerListCreateView(generics.ListCreateAPIView):
    queryset = TrashContainer.objects.all()
    serializer_class = TrashContainerSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        building = request.query_params['building'] if 'building' in request.query_params else None
        year = request.query_params['year'] if 'year' in request.query_params else None
        week = request.query_params['week'] if 'week' in request.query_params else None

        if building is not None and year is not None and week is not None:
            try:
                week_planning = WeekPlanning.objects.get(
                    week=week,
                    year=year
                )
                trash_templates = week_planning.trash_templates.all()
                trash_ids = None
                for trash in trash_templates:
                    buildings = [b.trash_ids for b in trash.buildings.all() if str(b.building.id) == building]
                    if len(buildings) != 0:
                        trash_ids = buildings[0]
                        break

                if trash_ids is None:
                    return Response(status=404)

                containers = TrashContainerIdWrapper.objects.filter(extra_id__in=[t.id for t in trash_ids.all()])
                data = TrashContainerSerializer([c.trash_container for c in containers], many=True).data
                return Response(data)
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
