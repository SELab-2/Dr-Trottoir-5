from .util import *
from planning.util import filter_templates, get_current_week_planning
from ronde.models import Building, LocatieEnum
from .serializers import *
from rest_framework.response import Response
import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def trash_templates_view(request):

    if request.method == "GET":
        templates = TrashContainerTemplate.objects.all()
        result = filter_templates(templates)
        data = TrashContainerTemplateSerializer(result, many=True).data
        return Response(data)

    if request.method == "POST":
        data = request.data
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()
        location = LocatieEnum.objects.get(id=data["location"])

        new_template = TrashContainerTemplate.objects.create(
            name=data["name"],
            even=data["even"],
            status=Status.ACTIEF,
            location=location,
            year=current_year,
            week=current_week
        )

        planning = get_current_week_planning()
        # voeg nieuwe template toe aan huidige planning als even/oneven matcht
        if new_template.even == (current_week % 2 == 0):
            planning.trash_templates.add(new_template)

        return Response({"message": "Success"})


@api_view(["DELETE", "GET"])
@permission_classes([AllowAny])
def trash_template_view(request, template_id):
    template = TrashContainerTemplate.objects.get(id=template_id)
    if request.method == "GET":
        return Response(TrashContainerTemplateSerializerFull(template).data)

    if request.method == "DELETE":
        current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()
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
    planning = get_current_week_planning()

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
    planning = get_current_week_planning()

    # Voeg de copy toe aan de huidige weekplanning
    planning.trash_templates.add(copy)

    # verwijder de oude template uit de weekplanning
    planning.trash_templates.remove(template)

    return Response({"message": "Success"})
