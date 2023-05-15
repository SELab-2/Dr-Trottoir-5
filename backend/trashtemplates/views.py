from .util import *

from planning.util import filter_templates, get_current_week_planning, get_current_time
from ronde.models import Building, LocatieEnum

from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def trash_templates_view(request):
    if request.method == "GET":
        """
        Geeft alle templates die niet inactief zijn terug.
        """
        templates = TrashContainerTemplate.objects.all()
        result = filter_templates(templates)
        data = TrashContainerTemplateSerializer(result, many=True).data
        return Response(data)

    if request.method == "POST":
        """
        Maakt een nieuwe TrashContainerTemplate aan.
        TODO checks
        """
        data = request.data
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

        add_if_match(get_current_week_planning().trash_templates, new_template, current_week)

        return Response({"id": new_template.id})


@api_view(["GET", "DELETE", "PATCH"])
@permission_classes([AllowAny])
def trash_template_view(request, template_id):
    template = get_trash_template(template_id)
    current_year, current_week = get_current_time()
    planning = get_current_week_planning()

    if request.method == "GET":
        """
        Geeft de TrashContainerTemplate terug.
        """
        return Response(TrashContainerTemplateSerializerFull(template).data)

    if request.method == "DELETE":
        """
        Verwijderd de TrashContainerTemplate.
        Als deze eenmalig was mag deze volledig uit de database verwijderd worden en moet degene die vervangen
        was terug actief gezet worden.
        """
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

    if request.method == "PATCH":
        """
        Past de TrashContainerTemplate aan.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """
        data = request.data
        permanent = data["permanent"]

        if "name" in data:
            pass
            # checks
        else:
            data["name"] = template.name

        if "even" in data:
            pass
            # checks
        else:
            data["even"] = template.even

        if "location" in data:
            data["location"] = LocatieEnum.objects.get(id=data["location"])
            # checks
        else:
            data["location"] = template.location

        if no_copy(template, permanent, current_year, current_week):
            template.name = data["name"]
            template.even = data["even"]
            template.location = data["location"]
            template.save()
            add_if_match(planning.trash_templates, template, current_week)
            return Response({"message": "Success"})

        new_template = TrashContainerTemplate.objects.create(
            name=data["name"],
            even=data["even"],
            status=Status.ACTIEF,
            location=data["location"],
            year=current_year,
            week=current_week
        )
        add_if_match(planning.trash_templates, new_template, current_week)

        # oude template op inactief zetten
        template.status = Status.INACTIEF
        template.save()
        remove_if_match(planning.trash_templates, template)

        return Response({"message": "Success"})


@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def trash_containers_view(request, template_id, permanent):
    template = get_trash_template(template_id)

    if request.method == "GET":
        """
        Geeft alle trash containers de template terug.
        """
        data = TrashContainerIdWrapperSerializer(template.trash_containers.all(), many=True).data
        return Response(data)

    if request.method == "POST":
        """
        Voegt de nieuwe TrashContainer toe aan de template adhv een TrashContainerIdWrapper.
        """
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


@api_view(["GET", "DELETE", "PATCH"])
@permission_classes([AllowAny])
def trash_container_view(request, template_id, extra_id, permanent):

    template = get_trash_template(template_id)
    tc_id_wrapper = template.trash_containers.get(extra_id=extra_id)

    if request.method == "GET":
        """
        Geeft een TrashContainer terug.
        """
        data = TrashContainerIdWrapperSerializer(tc_id_wrapper).data
        return Response(data)

    if request.method == "DELETE":
        """
        Verwijderd de TrashContainer van de template.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """

        update(
            template,
            "trash_containers",
            tc_id_wrapper,
            None,
            permanent,
            get_current_week_planning().trash_templates
        )
        return Response({"message": "Success"})

    if request.method == "PATCH":
        """
        Past een TrashContainer aan.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """
        data = request.data

        if "day" not in data:
            data["day"] = tc_id_wrapper.trash_container.collection_day.day

        if "start_hour" not in data:
            data["start_hour"] = tc_id_wrapper.trash_container.collection_day.start_hour

        if "end_hour" not in data:
            data["end_hour"] = tc_id_wrapper.trash_container.collection_day.end_hour

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


@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def buildings_view(request, template_id, permanent):
    data = request.data

    template = get_trash_template(template_id)

    if request.method == "GET":
        """
        Geeft alle gebouwen van deze template terug samen met hun selecties.
        """
        data = BuildingTrashContainerListSerializer(template.buildings.all(), many=True).data
        return Response(data)

    if request.method == "POST":
        """
        Voegt een nieuw gebouw samen met zijn selectie toe aan de template.
        """
        # checks
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
            get_current_week_planning().student_templates
        )
        return Response({"message": "Success"})


@api_view(["GET", "DELETE", "PATCH"])
@permission_classes([AllowAny])
def building_view(request, template_id, building_id, permanent):

    template = get_trash_template(template_id)
    building_list = template.buildings.get(building=building_id)

    if request.method == "GET":
        """
        Geeft het gebouw met zijn selectie terug.
        """
        data = BuildingTrashContainerListSerializer(building_list).data
        return Response(data)

    if request.method == "DELETE":
        """
        Verwijderd het gebouw en zijn selectie van de template.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """
        update(
            template,
            "buildings",
            building_list,
            None,
            permanent,
            get_current_week_planning().student_templates
        )

        return Response({"message": "Success"})

    if request.method == "PATCH":
        """
        Past de selectie van een gebouw aan.
        Neemt een copy van de template om de geschiedenis te behouden als dit nodig is.
        """
        data = request.data

        new_building_list = make_new_building_list(building_id, data["selection"])

        update(
            template,
            "buildings",
            building_list,
            new_building_list,
            permanent,
            get_current_week_planning().student_templates
        )
        return Response({"message": "Success"})
