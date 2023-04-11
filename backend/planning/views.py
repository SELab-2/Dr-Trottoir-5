from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from users.permissions import StudentReadOnly, AdminPermission, SuperstudentPermission, StudentPermission
import datetime
from trashtemplates.models import Status, TrashContainerTemplate
from ronde.models import LocatieEnum, Ronde
from ronde.serializers import RondeSerializer
from pickupdays.models import WeekDayEnum, PickUpDay
from .util import *

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class BuildingPictureCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]

    # TODO: a user can only see the pictures that he added (?)

    def post(self, request, *args, **kwargs):
        try:
            InfoPerBuilding.objects.get(pk=request.data["infoPerBuilding"])
        except InfoPerBuilding.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "infoPerBuilding"
                        }
                    ]
                }, code='invalid')
        return super().post(request=request, args=args, kwargs=kwargs)


class BuildingPictureRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]
    # TODO: only the user that created a BuildingPicture should be able to update it


class InfoPerBuildingCLAPIView(generics.ListCreateAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]

    # TODO: a user can only see the info per building that he added (?)

    def get(self, request, *args, **kwargs):
        dagPlanning = request.query_params['dagPlanning'] if 'dagPlanning' in request.query_params else None

        if dagPlanning is not None:
            try:
                DagPlanning.objects.get(pk=dagPlanning)
                self.queryset = InfoPerBuilding.objects.filter(dagPlanning=dagPlanning)
            except Exception:
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "referenced pk not in db", "field": "dagPlanning"
                            }
                        ]
                    }, code='invalid')

        return super().get(request=request, args=args, kwargs=kwargs)

    def post(self, request, *args, **kwargs):
        try:
            DagPlanning.objects.get(pk=request.data["dagPlanning"])
        except DagPlanning.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "dagPlanning"
                        }
                    ]
                }, code='invalid')
        return super().post(request=request, args=args, kwargs=kwargs)


class InfoPerBuildingRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InfoPerBuilding.objects.all()
    serializer_class = InfoPerBuildingSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]
    # TODO: only the user that created an InfoPerBuilding should be able to update it


@api_view(["GET"])
@permission_classes([AllowAny])
def week_planning_view(request, year, week):
    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    if year > current_year or (current_year == year and week > current_week):
        # dit is een week die nog moet komen dus geven we alleen de actieve of nu tijdelijk vervangen templates terug
        student_templates = StudentTemplate.objects.filter(status=Status.ACTIEF) | StudentTemplate.objects.filter(
            status=Status.VERVANGEN)
    else:
        # weekplanning is al voorbij of bezig
        week_planning = WeekPlanning.objects.get(
            week=week,
            year=year
        )
        student_templates = week_planning.student_templates.all()

    even = week % 2 == 0
    student_templates = student_templates.filter(even=even)
    data = StudentTemplateSerializer(student_templates, many=True).data
    return Response(data)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def student_templates_view(request):
    if request.method == "GET":
        templates = StudentTemplate.objects.all()
        result = filter_templates(templates)
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()
        data = StudentTemplateSerializer(result, many=True).data
        return Response(data)

    if request.method == "POST":
        data = request.data
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()
        location = LocatieEnum.objects.get(id=data["location"])

        new_template = StudentTemplate.objects.create(
            name=data["name"],
            even=data["even"],
            status=Status.ACTIEF,
            location=location,
            start_hour=data["start_hour"],
            end_hour=data["end_hour"],
            year=current_year,
            week=current_week
        )

        planning = get_current_week_planning()
        # voeg nieuwe template toe aan huidige planning
        planning.student_templates.add(new_template)
        data = StudentTemplateSerializer(new_template).data
        return Response(data)


@api_view(["GET", "DELETE"])
@permission_classes([AllowAny])
def student_template_view(request, template_id):
    template = StudentTemplate.objects.get(id=template_id)
    if request.method == "GET":
        return Response(StudentTemplateSerializer(template).data)

    if request.method == "DELETE":
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()
        planning = get_current_week_planning()

        if template.status == Status.EENMALIG:
            # template was eenmalig dus de originele template moet terug actief gemaakt worden
            original = StudentTemplate.objects.get(
                name=template.name,
                status=Status.VERVANGEN
            )
            original.status = Status.ACTIEF
            original.save()

            # voeg de originele terug toe aan de huidige weekplanning
            planning.student_templates.add(original)
            # verwijder de oude uit de huidige planning
            planning.student_templates.remove(template)
            # verwijder hem ook uit de database omdat hij eenmalig was en dus niet nodig is voor de geschiedenis
            template.delete()
        else:
            template.status = Status.INACTIEF
            template.save()
            planning.student_templates.remove(template)

        return Response({"message": "Success"})


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def rondes_view(request, template_id):
    template = StudentTemplate.objects.get(id=template_id)

    if request.method == "GET":
        data = RondeSerializer(template.rondes.all(), many=True).data
        return Response(data)

    if request.method == "POST":
        data = request.data
        method = data["method"]  # add of delete
        permanent = data["permanent"]
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

        ronde = Ronde.objects.get(id=data["ronde"])

        if template.status == Status.VERVANGEN or template.status == Status.INACTIEF:
            # templates met deze status mogen niet aangepast worden
            return Response({"error": "Mag niet"})

        if method == "delete":
            to_remove = template.dag_planningen.filter(ronde=ronde)

            if template.status == Status.EENMALIG or (
                    permanent and template.week == current_week and template.year == current_year):
                # als de template eenmalig is moet deze niet gekopieerd worden
                # ook wanneer het een permanente aanpassing is op een actieve template die deze week is aangemaakt
                template.dag_planningen.remove(*to_remove)
                template.rondes.remove(ronde)
                return Response({"message": "Success"})

            copy = make_copy(template, permanent, current_year, current_week)
            copy.dag_planningen.remove(*to_remove)
            copy.rondes.remove(ronde)
            return Response({"message": "Success"})

        # method == "add"
        dag_planningen = []
        for day in WeekDayEnum:
            dag_planning = make_dag_planning(day, template.start_hour, template.end_hour, data["ronde"], [])
            dag_planningen.append(dag_planning)

        if template.status == Status.EENMALIG or (
                permanent and template.week == current_week and template.year == current_year):
            # als de template eenmalig is moet deze niet gekopieerd worden
            # ook wanneer het een permanente aanpassing is op een actieve template die deze week is aangemaakt
            template.rondes.add(ronde)
            template.dag_planningen.add(*dag_planningen)
            return Response({"message": "Success"})

        copy = make_copy(template, permanent, current_year, current_week)
        copy.rondes.add(ronde)
        copy.dag_planningen.add(*dag_planningen)
        return Response({"message": "Success"})


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def dagplanning_view(request, template_id, ronde_id):
    template = StudentTemplate.objects.get(id=template_id)
    ronde = Ronde.objects.get(id=ronde_id)

    if request.method == "GET":
        dag_planningen = template.dag_planningen.filter(ronde=ronde_id)
        data = DagPlanningSerializer(dag_planningen, many=True).data
        return Response(data)

    data = request.data
    permanent = data["permanent"]
    method = data["method"]
    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    old_dag_planningen = template.dag_planningen.all()

    if template.status == Status.EENMALIG or (
            permanent and template.week == current_week and template.year == current_year):

        if method == "delete":
            delete_old_dag_planning(old_dag_planningen, data["day"], template)
            return Response({"message": "Success"})

        for new_dag_planning in data["dag_planningen"]:
            delete_old_dag_planning(old_dag_planningen, new_dag_planning["day"], template)
            dag_planning = make_dag_planning(new_dag_planning["day"], new_dag_planning["start_hour"],
                                             new_dag_planning["end_hour"], ronde_id, new_dag_planning["students"])
            template.dag_planningen.add(dag_planning)
        return Response({"message": "Success"})

    copy = make_copy(template, permanent, current_year, current_week)

    if method == "delete":
        delete_old_dag_planning(old_dag_planningen, data["day"], copy)
        return Response({"message": "Success"})

    for new_dag_planning in data["dag_planningen"]:
        delete_old_dag_planning(old_dag_planningen, new_dag_planning["day"], copy)
        dag_planning = make_dag_planning(new_dag_planning["day"], new_dag_planning["start_hour"],
                                         new_dag_planning["end_hour"], ronde, new_dag_planning["students"])
        copy.dag_planningen.add(*dag_planning)
    return Response({"message": "Success"})
