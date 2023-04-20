from pickupdays.models import WeekDayEnum
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ronde.models import LocatieEnum, Ronde
from ronde.serializers import RondeSerializer
from trashtemplates.models import Status
from trashtemplates.util import add_if_match, remove_if_match, no_copy, update
from users.permissions import StudentReadOnly, AdminPermission, SuperstudentPermission, StudentPermission

from .util import *


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
            ronde = Ronde.objects.get(pk=request.data["ronde"])
            response = super().post(request=request, args=args, kwargs=kwargs)
            dagPlanning = DagPlanning.objects.get(pk=response.data["id"])

            # Make a list of InfoPerBuilding and statuses
            for _ in ronde.buildings.all():
                InfoPerBuilding(dagPlanning=dagPlanning).save()
                dagPlanning.status.append('NS')
            dagPlanning.save()
            return response
        except WeekPlanning.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "referenced pk not in db", "field": "weekPlanning"
                        }
                    ]
                }, code='invalid')
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DagPlanningRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DagPlanning.objects.all()
    serializer_class = DagPlanningSerializerFull
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]


class BuildingPictureCreateAndListAPIView(generics.ListCreateAPIView):
    queryset = BuildingPicture.objects.all()
    serializer_class = BuildingPictureSerializer
    permission_classes = [StudentPermission | AdminPermission | SuperstudentPermission]

    # TODO: a user can only see the pictures that he added (?)

    def get(self, request, *args, **kwargs):
        infoPerBuilding = request.query_params['infoPerBuilding'] if 'infoPerBuilding' in request.query_params else None

        if infoPerBuilding is not None:
            try:
                InfoPerBuilding.objects.get(pk=infoPerBuilding)
                self.queryset = BuildingPicture.objects.filter(infoPerBuilding=infoPerBuilding)
            except Exception:
                raise serializers.ValidationError(
                    {
                        "errors": [
                            {
                                "message": "referenced pk not in db", "field": "infoPerBuilding"
                            }
                        ]
                    }, code='invalid')

        return super().get(request=request, args=args, kwargs=kwargs)

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


def get_student_templates(year, week):
    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    if year > current_year or (current_year == year and week > current_week):
        # dit is een week die nog moet komen dus geven we alleen de actieve of nu tijdelijk vervangen templates terug
        student_templates = StudentTemplate.objects.filter(status=Status.ACTIEF) | StudentTemplate.objects.filter(
            status=Status.VERVANGEN)
        even = week % 2 == 0
        student_templates = student_templates.filter(even=even)
    else:
        # weekplanning is al voorbij of bezig
        week_planning = WeekPlanning.objects.get(
            week=week,
            year=year
        )
        student_templates = week_planning.student_templates.all()

    return student_templates


@api_view(["GET"])
@permission_classes([AllowAny])
def week_planning_view(request, year, week):
    student_templates = get_student_templates(year, week)
    data = StudentTemplateSerializer(student_templates, many=True).data
    return Response(data)


@api_view(["GET"])
@permission_classes([AdminPermission | SuperstudentPermission | AllowAny])
def student_templates_rondes_view(request, year, week, day, location):
    if request.method == "GET":
        if day < 0 or day > 6:
            return Response(status=400)
        days = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']
        day_name = days[day]

        templates = get_student_templates(year, week).filter(location=location)
        planned = []
        for template in templates:
            dag_planningen = template.dag_planningen.all()
            planned += [x for x in dag_planningen if x.time.day == day_name]
        planned = list(dict.fromkeys(planned))
        planned = DagPlanningSerializerFull(planned, many=True).data
        return Response(planned)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def student_templates_view(request):
    if request.method == "GET":
        """
        Geeft alle templates die niet inactief zijn terug.
        """
        templates = StudentTemplate.objects.all()
        result = filter_templates(templates)
        data = StudentTemplateSerializer(result, many=True).data
        return Response(data)

    if request.method == "POST":
        """
        Maakt een nieuwe StudentTemplate aan.
        TODO checks
        """
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

        add_if_match(get_current_week_planning().student_templates, new_template, current_week)
        return Response({"message": "Success", "new_id": new_template.id})


@api_view(["GET", "DELETE", "PATCH"])
@permission_classes([AllowAny])
def student_template_view(request, template_id):
    template = StudentTemplate.objects.get(id=template_id)
    if request.method == "GET":
        """
        Geeft de StudentTemplate terug.
        """
        return Response(StudentTemplateSerializer(template).data)
    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    if request.method == "DELETE":
        """
        Verwijderd de StudentTemplate.
        Als deze eenmalig was mag deze volledig uit de database verwijderd worden en moet degene die vervangen
        was terug actief gezet worden.
        """
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

    if request.method == "PATCH":
        """
        Past de StudentTemplate aan.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """
        data = request.data

        if "name" not in data:
            data["name"] = template.name

        if "even" not in data:
            data["even"] = template.even

        if "location" not in data:
            data["location"] = template.location
        else:
            data["location"] = LocatieEnum.objects.get(id=data["location"])

        if "start_hour" not in data:
            data["start_hour"] = template.start_hour
        else:
            start_hour = [int(t) for t in data["start_hour"].split(":")]
            data["start_hour"] = datetime.time(start_hour[0], start_hour[1])

        if "end_hour" not in data:
            data["end_hour"] = template.end_hour
        else:
            end_hour = [int(t) for t in data["end_hour"].split(":")]
            data["end_hour"] = datetime.time(end_hour[0], end_hour[1])

        validate_student_template_data(data)

        planning = get_current_week_planning()

        response = {"message": "Success"}
        if no_copy(template, True, current_year, current_week):
            template.name = data["name"]
            template.even = data["even"]
            template.location = data["location"]
            # template.start_hour = data["start_hour"]
            # template.end_hour = data["end_hour"],
            template.save()
            add_if_match(planning.student_templates, template, current_week)
            return Response(response)

        new_template = StudentTemplate.objects.create(
            name=data["name"],
            even=data["even"],
            status=Status.ACTIEF,
            location=data["location"],
            start_hour=data["start_hour"],
            end_hour=data["end_hour"],
            year=current_year,
            week=current_week
        )
        add_if_match(planning.student_templates, new_template, current_week)

        # oude template op inactief zetten
        template.status = Status.INACTIEF
        template.save()
        remove_if_match(planning.student_templates, template, current_week)
        response["new_id"] = new_template.id
        return Response(response)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def rondes_view(request, template_id):
    template = StudentTemplate.objects.get(id=template_id)

    if request.method == "GET":
        """
        Geeft alle rondes van deze template terug.
        """
        data = RondeSerializer(template.rondes.all(), many=True).data
        return Response(data)

    if request.method == "POST":
        """
        Voegt een nieuwe Ronde toe aan de template.
        """
        data = request.data
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

        ronde = Ronde.objects.get(id=data["ronde"])

        dag_planningen = []

        data["start_hour"] = template.start_hour
        data["end_hour"] = template.end_hour
        data["students"] = []
        for day in WeekDayEnum:
            data["day"] = day
            dag_planning = make_dag_planning(data)
            dag_planningen.append(dag_planning)

        response = {"message": "Success"}
        if no_copy(template, True, current_year, current_week):
            template.rondes.add(ronde)
            template.dag_planningen.add(*dag_planningen)
        else:
            copy = make_copy(template, True, current_year, current_week)
            copy.rondes.add(ronde)
            copy.dag_planningen.add(*dag_planningen)
            remove_if_match(get_current_week_planning().student_templates, template, current_week)
            add_if_match(get_current_week_planning().student_templates, copy, current_week)
            response["new_id"] = copy.id

        return Response(response)


@api_view(["DELETE"])
@permission_classes([AllowAny])
def ronde_view(request, template_id, ronde_id):
    template = StudentTemplate.objects.get(id=template_id)
    ronde = Ronde.objects.get(id=ronde_id)

    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    if request.method == "DELETE":
        """
        Verwijderd een ronde en al zijn dagplanningen uit de template.
        """
        to_remove = template.dag_planningen.filter(ronde=ronde)

        response = {"message": "Success"}
        if no_copy(template, True, current_year, current_week):
            template.dag_planningen.remove(*to_remove)
            template.rondes.remove(ronde)
        else:
            copy = make_copy(template, True, current_year, current_week)
            copy.dag_planningen.remove(*to_remove)
            copy.rondes.remove(ronde)
            remove_if_match(get_current_week_planning().student_templates, template, current_week)
            add_if_match(get_current_week_planning().student_templates, copy, current_week)
            response["new_id"] = copy.id
        return Response(response)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def dagplanningen_view(request, template_id, ronde_id):
    template = StudentTemplate.objects.get(id=template_id)

    if request.method == "GET":
        """
        Geeft alle dagplanningen van een ronde terug.
        """
        dag_planningen = template.dag_planningen.filter(ronde=ronde_id)
        data = DagPlanningSerializer(dag_planningen, many=True).data
        return Response(data)

    if request.method == "POST":
        """
        Maakt een nieuwe DagPlanning aan.
        """
        data = request.data
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

        data["ronde"] = ronde_id
        validate_dag_planning_data(data)
        new_dag_planning = make_dag_planning(data)

        response = update(
            template,
            "dag_planningen",
            None,
            new_dag_planning,
            True,
            get_current_week_planning().student_templates,
            copy_template=make_copy
        )
        response["message"] = "Success"
        return Response(response)


@api_view(["GET", "DELETE", "PATCH"])
@permission_classes([AllowAny])
def dagplanning_view(request, template_id, dag_id, permanent):

    template = StudentTemplate.objects.get(id=template_id)

    dag_planning = DagPlanning.objects.get(id=dag_id)
    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    if request.method == "GET":
        """
        Geeft een dagplanning terug
        """
        data = DagPlanningSerializer(dag_planning).data
        return Response(data)

    if request.method == "DELETE":
        """
        Verwijder een DagPlanning van de template
        """

        response = update(
            template,
            "dag_planningen",
            dag_planning,
            None,
            permanent,
            get_current_week_planning().student_templates,
            copy_template=make_copy
        )
        response["message"] = "Success"
        return Response(response)

    if request.method == "PATCH":
        """
        Verander de studenten voor een DagPlanning
        """
        data = request.data

        data["day"] = dag_planning.time.day
        if "start_hour" not in data:
            data["start_hour"] = dag_planning.time.start_hour
        if "end_hour" not in data:
            data["end_hour"] = dag_planning.time.end_hour
        if "ronde" not in data:
            data["ronde"] = dag_planning.ronde.id
        if "students" not in data:
            data["students"] = dag_planning.students.all()

        new_dag_planning = make_dag_planning(data)

        response = update(
            template,
            "dag_planningen",
            dag_planning,
            new_dag_planning,
            permanent,
            get_current_week_planning().student_templates,
            copy_template=make_copy
        )
        response["message"] = "Success"
        return Response(response)
