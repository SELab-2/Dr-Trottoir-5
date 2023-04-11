from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from users.permissions import StudentReadOnly, AdminPermission, SuperstudentPermission, StudentPermission
import datetime
from trashtemplates.models import Status
from ronde.models import LocatieEnum, Ronde
from ronde.serializers import RondeSerializer
from pickupdays.models import WeekDayEnum, PickUpDay

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class DagPlanningCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        student = request.query_params['student'] if 'student' in request.query_params else None
        date = request.query_params['date'] if 'date' in request.query_params else None

        if student is not None and date is not None:
            try:
                dagPlanning = DagPlanning.objects.get(student=student, date=date)
                return Response(DagPlanningSerializerFull(dagPlanning).data)
            except DagPlanning.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "referenced pk not in db", "field": "dagPlanning"
                            }
                        ]
                    }, code='invalid')
        elif student is not None:
            try:
                dagPlanning = DagPlanning.objects.get(student=student)
                return Response(DagPlanningSerializerFull(dagPlanning).data)
            except DagPlanning.DoesNotExist:
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
            WeekPlanning.objects.get(pk=request.data["weekPlanning"])
        except WeekPlanning.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "weekPlanning"
                        }
                    ]
                }, code='invalid')
        return super().post(request=request, args=args, kwargs=kwargs)


class DagPlanningRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]


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


class WeekPlanningCLAPIView(generics.ListCreateAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]


class WeekPlanningRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeekPlanning.objects.all()
    serializer_class = WeekPlanningSerializer
    permission_classes = [StudentReadOnly | AdminPermission | SuperstudentPermission]



def make_copy(template, permanent, current_year, current_week):
    """
        Neemt een copy van een template zodat de geschiedenis behouden wordt
    """

    copy = StudentTemplate.objects.create(
        name=template.name,
        even=template.even,
        status=Status.ACTIEF if permanent else Status.EENMALIG,
        location=template.location,
        year=current_year,
        week=current_week
    )
    copy.rondes.set(template.rondes.all())
    copy.dag_planningen.set(template.dag_planningen.all())

    # verander de status van de nu oude template
    template.status = Status.INACTIEF if permanent else Status.VERVANGEN
    template.week = current_week
    template.save()

    return copy


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def student_templates_view(request):

    if request.method == "GET":
        templates = StudentTemplate.objects.all()
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

        for template in templates:
            is_current = template.week == current_week or template.year == current_year
            # template was tijdelijk veranderd maar de week is voorbij dus nu geldt deze weer
            if template.status == Status.VERVANGEN and not is_current:
                template.status = Status.ACTIEF
                template.save()
            # template was tijdelijk maar de week is voorbij dus nu geldt deze niet meer
            elif template.status == Status.EENMALIG and not is_current:
                template.status = Status.INACTIEF
                template.save()

        result = templates.filter(status=Status.ACTIEF) | templates.filter(status=Status.EENMALIG) | templates.filter(
            status=Status.VERVANGEN)
        data = StudentTemplateSerializer(result, many=True).data
        return Response(data)

    if request.method == "POST":
        data = request.data
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()
        location = LocatieEnum.objects.get(id=data["location"])

        new_template = StudentTemplate.objects.create(
            name=data["name"],
            even=data["even"].lower() == "true",
            status=Status.ACTIEF,
            location=location,
            year=current_year,
            week=current_week
        )

        planning, _ = WeekPlanning.objects.get_or_create(
            week=current_week,
            year=current_year
        )
        # voeg nieuwe template toe aan huidige planning
        planning.student_templates.add(new_template)
        data = StudentTemplateSerializer(new_template).data
        return Response(data)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def rondes_view(request, template_id):
    template = StudentTemplate.objects.get(id=template_id)

    if request.method == "GET":
        data = RondeSerializer(template.rondes.all()).data
        return Response(data)

    if request.method == "POST":
        data = request.data
        method = data["method"] # add of delete
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
                template.dag_planningen.remove(to_remove)
                template.rondes.remove(ronde)
                return Response({"message": "Success"})

            copy = make_copy(template, permanent, current_week, current_year)
            copy.dag_planningen.remove(to_remove)
            copy.rondes.remove(to_remove)
            return Response({"message": "Success"})

        # method == "add"
        dag_planningen = []
        for day in WeekDayEnum:
            pickup_day, _ = PickUpDay.objects.get_or_create(
                day=day,
                start_hour="17:00",
                end_hour="20:00"
            )
            dag_planning, _ = DagPlanning.objects.get_or_create(
                ronde=ronde,
                weekday=pickup_day,
                students=[]
            )
            dag_planningen.append(dag_planning)

        if template.status == Status.EENMALIG or (
                permanent and template.week == current_week and template.year == current_year):
        # als de template eenmalig is moet deze niet gekopieerd worden
        # ook wanneer het een permanente aanpassing is op een actieve template die deze week is aangemaakt
            template.rondes.add(ronde)
            template.dag_planningen.add(dag_planningen)
            return Response({"message": "Success"})

        copy = make_copy(template, permanent, current_week, current_year)
        copy.rondes.add(ronde)
        copy.dag_planningen.add(dag_planningen)
        return Response({"message": "Success"})



