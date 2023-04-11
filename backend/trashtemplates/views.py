from rest_framework import generics
from .models import *
from trashcontainers.models import TrashContainer
from planning.models import WeekPlanning
from pickupdays.models import PickUpDay
from ronde.models import Building, LocatieEnum
from .serializers import *
from rest_framework.response import Response
import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def make_new_tc_id_wrapper(data, extra_id):
    """
        Maakt nieuwe TrashContainerIdWrapper aan
    """
    # maak nieuwe pickupday met de aangepaste data
    new_pickup_day, _ = PickUpDay.objects.get_or_create(
        day=data["day"],
        start_hour=data["start_hour"],
        end_hour=data["end_hour"]
    )

    # maak nieuwe container met de net gemaakte pickupday
    new_trash_container, _ = TrashContainer.objects.get_or_create(
        type=data["type"],
        collection_day=new_pickup_day
    )

    # maak een wrapper met een het gegeven extra id en de nieuwe trashcontainer
    tc_id_wrapper, _ = TrashContainerIdWrapper.objects.get_or_create(
        extra_id=extra_id,
        trash_container=new_trash_container
    )
    return tc_id_wrapper


def make_copy(template, permanent, current_year, current_week):
    """
        Neemt een copy van een template zodat de geschiedenis behouden wordt
    """

    copy = TrashContainerTemplate.objects.create(
        name=template.name,
        even=template.even,
        status=Status.ACTIEF if permanent else Status.EENMALIG,
        location=template.location,
        year=current_year,
        week=current_week
    )
    copy.buildings.set(template.buildings.all())
    copy.trash_containers.set(template.trash_containers.all())

    # verander de status van de nu oude template
    template.status = Status.INACTIEF if permanent else Status.VERVANGEN
    template.week = current_week
    template.save()

    return copy


def update_many_to_many(many_to_many, old, new):
    if old is not None:
        many_to_many.remove(old)

    if new is not None:
        many_to_many.add(new)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def trash_templates_view(request):

    if request.method == "GET":
        templates = TrashContainerTemplate.objects.all()
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
        data = TrashContainerTemplateSerializer(result, many=True).data
        return Response(data)

    if request.method == "POST":
        data = request.data
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()
        location = LocatieEnum.objects.get(id=data["location"])

        new_template = TrashContainerTemplate.objects.create(
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
        planning.trash_templates.add(new_template)
        data = TrashContainerTemplateSerializer(new_template).data
        return Response(data)


@api_view(["DELETE", "GET"])
@permission_classes([AllowAny])
def trash_template_view(request, template_id):
    template = TrashContainerTemplate.objects.get(id=template_id)
    if request.method == "GET":
        return Response(TrashContainerTemplateSerializerFull(template).data)

    if request.method == "DELETE":
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()
        planning, _ = WeekPlanning.objects.get_or_create(
            week=current_week,
            year=current_year
        )

        if template.status == Status.EENMALIG:
            # template was eenmalig dus de originele template moet terug actief gemaakt worden
            original = TrashContainerTemplate.objects.get(
                name=template.name,
                status=Status.VERVANGEN
            )
            original.status = Status.ACTIEF
            original.save()

            # voeg de originele terug toe aan de huidige weekplanning
            planning.trash_templates.add(original)
            # verwijder de oude uit de huidige planning
            planning.trash_templates.remove(template)
            # verwijder hem ook uit de database omdat hij eenmalig was en dus niet nodig is voor de geschiedenis
            template.delete()
        else:
            template.status = Status.INACTIEF
            template.save()
            planning.trash_templates.remove(template)

        return Response({"message": "Success"})


@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def trash_container_view(request, template_id):
    data = request.data

    template = TrashContainerTemplate.objects.get(id=template_id)

    if request.method == "GET":  # give list of all trash containers
        data = TrashContainerIdWrapperSerializer(template.trash_containers.all(), many=True).data
        return Response(data)

    if template.status == Status.VERVANGEN or template.status == Status.INACTIEF:
        # templates met deze status mogen niet aangepast worden
        return Response({"error": "Mag niet"})

    permanent = data["permanent"]
    method = data["method"]  # add, edit of delete

    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    # alleen bij add moet er een nieuwe ExtraId aangemaakt worden
    extra_id = ExtraId.objects.create() if method == "add" else ExtraId.objects.get(id=data["extra_id"])

    # alleen bij edit en remove moet er een oude copy verwijderd worden
    to_remove = None if method == "add" else template.trash_containers.get(extra_id=extra_id)

    # alleen bij edit en add moet er een nieuwe TrashContainerIdWrapper gemaakt worden
    tc_id_wrapper = None if method == "delete" else make_new_tc_id_wrapper(data, extra_id)

    if template.status == Status.EENMALIG or (
            permanent and template.week == current_week and template.year == current_year):
        # als de template eenmalig is moet deze niet gekopieerd worden
        # ook wanneer het een permanente aanpassing is op een actieve template die deze week is aangemaakt

        # verwijder de oude en voeg de nieuwe toe
        update_many_to_many(template.trash_containers, to_remove, tc_id_wrapper)

        return Response({"message": "Success"})

    # neem copy om de geschiedenis te behouden
    copy = make_copy(template, permanent, current_year, current_week)

    # verwijder de oude en voeg de nieuwe toe
    update_many_to_many(copy.trash_containers, to_remove, tc_id_wrapper)

    # zoek de weekplanning van deze week
    planning, created = WeekPlanning.objects.get_or_create(
        week=current_week,
        year=current_year
    )

    # Voeg de copy toe aan de huidige weekplanning
    planning.trash_templates.add(copy)

    # verwijder de oude template uit de weekplanning
    planning.trash_templates.remove(template)

    return Response({"message": "Success"})


@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def building_view(request, template_id):
    data = request.data

    template = TrashContainerTemplate.objects.get(id=template_id)

    if request.method == "GET":  # give list of all buildings
        data = BuildingTrashContainerListSerializer(template.buildings.all(), many=True).data
        return Response(data)

    if template.status == Status.VERVANGEN or template.status == Status.INACTIEF:
        # templates met deze status mogen niet aangepast worden
        return Response({"error": "Mag niet"})

    permanent = data["permanent"]
    method = data["method"]  # add, edit of delete

    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    # alleen bij add method is er geen oude die verwijderd moet worden
    old_building_list = None if method == "add" else template.buildings.get(building=data["building"])

    new_building_list = None
    if method != "delete":  # alleen bij add en edit moet een nieuwe gemaakt worden
        building = Building.objects.get(id=data["building"])
        new_building_list = BuildingTrashContainerList.objects.create(
            building=building
        )
        new_building_list.trash_ids.set(data["selection"])

    if template.status == Status.EENMALIG or (
            permanent and template.week == current_week and template.year == current_year):
        # als de template eenmalig is moet deze niet gekopieerd worden
        # ook wanneer het een permanente aanpassing is op een actieve template die deze week is aangemaakt

        # verwijder de oude en voeg de nieuwe toe
        update_many_to_many(template.buildings, old_building_list, new_building_list)

        return Response({"message": "Success"})

    # neem copy om de geschiedenis te behouden
    copy = make_copy(template, permanent, current_year, current_week)

    # verwijder de oude en voeg de nieuwe toe
    update_many_to_many(copy.buildings, old_building_list, new_building_list)

    # zoek de weekplanning van deze week
    planning, created = WeekPlanning.objects.get_or_create(
        week=current_week,
        year=current_year
    )

    # Voeg de copy toe aan de huidige weekplanning
    planning.trash_templates.add(copy)

    # verwijder de oude template uit de weekplanning
    planning.trash_templates.remove(template)

    return Response({"message": "Success"})
