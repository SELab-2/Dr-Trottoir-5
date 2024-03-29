from rest_framework import generics
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from planning.util import filter_templates, get_current_week_planning, get_current_time
from trashcontainers.serializers import TrashContainerSerializer
from users.permissions import *
from ronde.models import LocatieEnum, Building
from planning.models import WeekPlanning
from .util import *
from exceptions.exceptionHandler import ExceptionHandler


class BuildingTrashPlan(generics.ListAPIView):
    permission_classes = [BewonerPermission | SyndicusPermission | StudentPermission | SuperstudentPermission | AdminPermission]

    def get(self, request, *args, **kwargs):
        """
        Geeft de vuilnisplanning voor een bepaalde week
        """
        year = kwargs.get("year")
        week = kwargs.get("week")
        templates = get_trash_templates(year, week)
        active_exists = 'A' in [t.status for t in templates]
        result = {}
        for template in templates:
            if (active_exists and template.status == 'A') or not active_exists:
                buildings = template.buildings.all()
                for building in buildings:
                    containers = template.trash_containers.filter(extra_id__in=building.trash_ids.all())
                    result[building.building.id] = TrashContainerSerializer([c.trash_container for c in containers], many=True).data
                break
        return Response(result)


def get_trash_templates(year, week):
    current_year, current_week = get_current_time()

    if year > current_year or (current_year == year and week > current_week):
        # dit is een week die nog moet komen dus geven we alleen de actieve of nu tijdelijk vervangen templates terug
        # buiten als de template vervangen is voor de volgende week
        trash_templates_actief = TrashContainerTemplate.objects.filter(
            status=Status.ACTIEF)
        trash_templates_vervangen = TrashContainerTemplate.objects.filter(
            status=Status.VERVANGEN).exclude(week=week, year=year)
        trash_templates_eenmalig = TrashContainerTemplate.objects.filter(
            status=Status.EENMALIG, week=week, year=year)

        even = week % 2 == 0
        trash_templates = trash_templates_actief | trash_templates_vervangen | trash_templates_eenmalig
        trash_templates = trash_templates.filter(even=even)
    else:
        # weekplanning is al voorbij of bezig
        get_current_week_planning()  # nodig voor moest de weekplanning nog niet gemaakt zijn
        try:
            week_planning = WeekPlanning.objects.get(
                week=week,
                year=year
            )
            trash_templates = week_planning.trash_templates.all()
        except WeekPlanning.DoesNotExist:
            trash_templates = []

    return trash_templates


class TrashTemplatesView(generics.RetrieveAPIView, generics.CreateAPIView):
    permission_classes = [SuperstudentPermission | AdminPermission]

    def get(self, request, *args, **kwargs):
        """
        Geeft alle templates die niet inactief zijn terug.
        """
        templates = TrashContainerTemplate.objects.all()
        result = filter_templates(templates)
        data = TrashContainerTemplateSerializer(result, many=True).data
        return Response(data)

    def post(self, request, *args, **kwargs):
        """
        Maakt een nieuwe TrashContainerTemplate aan.
        """
        data = request.data
        handler = ExceptionHandler()
        handler.check_not_blank_required(data.get("name"), "name")
        handler.check_boolean_required(data.get("even"), "even")
        handler.check_primary_key_value_required(data.get("location"), "location", LocatieEnum)
        handler.check()

        current_year, current_week = get_current_time()
        location = LocatieEnum.objects.get(id=data["location"])

        new_template = TrashContainerTemplate.objects.create(
            name=data["name"],
            even=data["even"],
            status=Status.ACTIEF,
            location=location,
            year=current_year,
            week=current_week
        )

        add_if_match(get_current_week_planning().trash_templates, new_template,
                     current_week)

        return Response({"id": new_template.id})


class TrashTemplateView(generics.RetrieveDestroyAPIView):
    permission_classes = [SuperstudentPermission | AdminPermission]

    def get(self, request, *args, **kwargs):
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])
        return Response(TrashContainerTemplateSerializerFull(template).data)

    def delete(self, request, *args, **kwargs):
        """
        Verwijderd de TrashContainerTemplate.
        Als deze eenmalig was mag deze volledig uit de database verwijderd worden en moet degene die vervangen
        was terug actief gezet worden.
        """
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])

        handler = ExceptionHandler()
        handler.check_vervangen(template)
        handler.check_not_inactive(template, "template")
        handler.check()

        current_year, current_week = get_current_time()
        planning = get_current_week_planning()
        if template.status == Status.EENMALIG:
            # template was eenmalig dus de originele template moet terug actief gemaakt worden
            original = TrashContainerTemplate.objects.get(
                name=template.name,
                status=Status.VERVANGEN
            )
            original.status = Status.ACTIEF
            original.save()

            # voeg de originele terug toe aan de huidige weekplanning
            add_if_match(planning.trash_templates, original, current_week)

            # verwijder de oude uit de huidige planning
            remove_if_match(planning.trash_templates, template)
            # verwijder hem ook uit de database omdat hij eenmalig was en dus niet nodig is voor de geschiedenis
            template.delete()
        else:
            template.status = Status.INACTIEF
            template.save()
            remove_if_match(planning.trash_templates, template)

        return Response({"message": "Success"})


class TrashContainersView(generics.CreateAPIView, generics.RetrieveAPIView):
    permission_classes = [AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        """
        Geeft alle trash containers de template terug.
        """
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])
        data = TrashContainerIdWrapperSerializer(
            template.trash_containers.all(), many=True).data
        return Response(data)

    def post(self, request, *args, **kwargs):
        """
        Voegt de nieuwe TrashContainer toe aan de template adhv een TrashContainerIdWrapper.
        """
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])
        handler = ExceptionHandler()
        handler.check_not_inactive(template, "template")
        handler.check()
        permanent = kwargs["permanent"]
        data = request.data

        extra_id = ExtraId.objects.create()
        new_tc_id_wrapper = make_new_tc_id_wrapper(data, extra_id)

        update(
            template,
            "trash_containers",
            None,
            new_tc_id_wrapper,
            permanent,
            get_current_week_planning().trash_templates
        )

        return Response({"message": "Success"})


class TrashContainerView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        """
        Geeft een TrashContainer terug.
        """
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])
        tc_id_wrapper = template.trash_containers.get(extra_id=kwargs[
            "extra_id"])
        data = TrashContainerIdWrapperSerializer(tc_id_wrapper).data
        return Response(data)

    def put(self, request, *args, **kwargs):
        raise ValidationError("no PUT allowed")

    def patch(self, request, *args, **kwargs):
        """
        Past een TrashContainer aan.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])
        handler = ExceptionHandler()
        handler.check_not_inactive(template, "template")
        handler.check()
        tc_id_wrapper = template.trash_containers.get(extra_id=kwargs[
            "extra_id"])
        permanent = kwargs["permanent"]
        data = request.data

        if "collection_day" not in data:
            data["collection_day"] = {}

        if "day" not in data.get("collection_day"):
            data["collection_day"]["day"] = tc_id_wrapper.trash_container.collection_day.day

        if "start_hour" not in data.get("collection_day"):
            data["collection_day"]["start_hour"] = tc_id_wrapper.trash_container.collection_day.start_hour

        if "end_hour" not in data.get("collection_day"):
            data["collection_day"]["end_hour"] = tc_id_wrapper.trash_container.collection_day.end_hour

        if "type" not in data:
            data["type"] = tc_id_wrapper.trash_container.type

        new_tc_id_wrapper = make_new_tc_id_wrapper(data, tc_id_wrapper.extra_id)

        update(
            template,
            "trash_containers",
            tc_id_wrapper,
            new_tc_id_wrapper,
            permanent,
            get_current_week_planning().trash_templates
        )

        return Response({"message": "Success"})

    def delete(self, request, *args, **kwargs):
        """
        Verwijderd de TrashContainer van de template.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])
        handler = ExceptionHandler()
        handler.check_not_inactive(template, "template")
        handler.check()
        tc_id_wrapper = template.trash_containers.get(extra_id=kwargs[
            "extra_id"])
        permanent = kwargs["permanent"]
        update(
            template,
            "trash_containers",
            tc_id_wrapper,
            None,
            permanent,
            get_current_week_planning().trash_templates
        )
        return Response({"message": "Success"})


class BuildingsView(generics.CreateAPIView, generics.RetrieveAPIView):
    permission_classes = [AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        """
        Geeft alle gebouwen van deze template terug samen met hun selecties.
        """
        template = TrashContainerTemplate.objects.get(id=kwargs[
            "template_id"])
        data = BuildingTrashContainerListSerializer(template.buildings.all(),
                                                    many=True).data
        return Response(data)

    def post(self, request, *args, **kwargs):
        """
        Voegt een nieuw gebouw samen met zijn selectie toe aan de template.
        """
        data = request.data
        template = TrashContainerTemplate.objects.get(id=kwargs[
            "template_id"])
        handler = ExceptionHandler()
        handler.check_not_inactive(template, "template")
        handler.check()

        permanent = kwargs["permanent"]
        building = Building.objects.get(id=data["building"])
        new_building_list = BuildingTrashContainerList.objects.create(
            building=building
        )
        new_building_list.trash_ids.set(data["selection"])

        update(
            template,
            "buildings",
            None,
            new_building_list,
            permanent,
            get_current_week_planning().trash_templates
        )
        return Response({"message": "Success"})


class BuildingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminPermission | SuperstudentPermission]

    def get(self, request, *args, **kwargs):
        """
        Geeft het gebouw met zijn selectie terug.
        """
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])
        building_list = template.buildings.get(building=kwargs["building_id"])
        new_list = []
        for trash_id in building_list.trash_ids.all():
            if template.trash_containers.filter(extra_id=trash_id).exists():
                new_list.append(trash_id)
        building_list.trash_ids.set(new_list)

        data = BuildingTrashContainerListSerializer(building_list).data
        return Response(data)

    def delete(self, request, *args, **kwargs):
        """
        Verwijderd het gebouw en zijn selectie van de template.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])
        handler = ExceptionHandler()
        handler.check_not_inactive(template, "template")
        handler.check()
        building_list = template.buildings.get(building=kwargs["building_id"])
        permanent = kwargs["permanent"]
        update(
            template,
            "buildings",
            building_list,
            None,
            permanent,
            get_current_week_planning().trash_templates
        )

        return Response({"message": "Success"})

    def patch(self, request, *args, **kwargs):
        """

        Past de selectie van een gebouw aan.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """
        data = request.data
        template = TrashContainerTemplate.objects.get(id=kwargs["template_id"])
        handler = ExceptionHandler()
        handler.check_not_inactive(template, "template")
        handler.check()

        building_list = template.buildings.get(building=kwargs["building_id"])
        permanent = kwargs["permanent"]
        new_building_list = make_new_building_list(kwargs["building_id"],
                                                   data["selection"])
        update(
            template,
            "buildings",
            building_list,
            new_building_list,
            permanent,
            get_current_week_planning().trash_templates
        )
        return Response({"message": "Success"})

    def put(self, request, *args, **kwargs):
        raise ValidationError("no PUT allowed")
