from rest_framework import generics
from .models import *
from trashcontainers.models import TrashContainer
from pickupdays.models import PickUpDay
from .serializers import TrashContainerTemplateSerializer
from rest_framework.response import Response
import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class TrashContainerTemplateListCreateView(generics.ListCreateAPIView):
    queryset = TrashContainerTemplate.objects.all()
    serializer_class = TrashContainerTemplateSerializer
    permission_classes = [AllowAny]


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
    tc_id_wrapper = TrashContainerIdWrapper.objects.create(
        extra_id=extra_id,
        trash_container=new_trash_container
    )
    return tc_id_wrapper


def make_copy(template, permanent, current_year, current_week):
    copy = TrashContainerTemplate.objects.create(
        name=template.name,
        even=template.even,
        status="actief" if permanent else "tijdelijk",
        year=current_year,
        week=current_week
    )
    copy.buildings.set(template.buildings.all())
    copy.trash_containers.set(template.trash_containers.all())

    # verander de status van de nu oude template
    template.status = "verwijderd" if permanent else "tijdelijk vervangen"
    template.week = current_week
    template.save()

    return copy

@api_view(["POST"])
@permission_classes([AllowAny])
def add_trash_container_view(request, template_id):
    data = request.data
    permanent = data["permanent"]

    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    template = TrashContainerTemplate.objects.get(id=template_id)

    # maak nieuwe TrashContainerIdWrapper
    tc_id_wrapper = make_new_tc_id_wrapper(data, ExtraId.objects.create())

    if permanent and template.week == current_week and template.year == current_year:
        # template is in deze week aangemaakt dus moet niet gekopieerd worden bij permanente aanpassing
        template.trash_containers.add(tc_id_wrapper)
        return Response({"message": "Afval container succesvol toegevoegd."})

    # neem een copy
    copy = make_copy(template, permanent, current_year, current_week)

    # voeg de nieuwe trashcontainer toe aan de copy
    copy.trash_containers.add(tc_id_wrapper)
    return Response({"message": "Afval container succesvol toegevoegd."})


@api_view(["POST"])
@permission_classes([AllowAny])
def edit_trash_container_view(request, template_id):
    data = request.data
    permanent = data["permanent"]

    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    template = TrashContainerTemplate.objects.get(id=template_id)

    # vind de oude versie van de trashcontainer
    extra_id = ExtraId.objects.get(id=data["extra_id"])
    to_remove = template.trash_containers.get(extra_id=extra_id)

    # maak de nieuwe TrashContainerIdWrapper
    tc_id_wrapper = make_new_tc_id_wrapper(data, extra_id)

    if permanent and template.week == current_week and template.year == current_year:
        # template is in deze week aangemaakt dus moet niet gekopieerd worden bij permanente aanpassing
        template.trash_containers.remove(to_remove)
        template.trash_containers.add(tc_id_wrapper)
        return Response({"message": "Afval container succesvol aangepast."})

    # neem copy
    copy = make_copy(template, permanent, current_year, current_week)

    # verwijder de oude trashcontainer en voeg de nieuwe toe
    copy.trash_containers.remove(to_remove)
    copy.trash_containers.add(tc_id_wrapper)

    return Response({"message": "Afval container succesvol aangepast."})


@api_view(["POST"])
@permission_classes([AllowAny])
def delete_trash_container_view(request, template_id):
    data = request.data
    permanent = data["permanent"]

    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    template = TrashContainerTemplate.objects.get(id=template_id)

    # vind de oude versie van de trashcontainer
    extra_id = ExtraId.objects.get(id=data["extra_id"])
    to_remove = template.trash_containers.get(extra_id=extra_id)


    if permanent and template.week == current_week and template.year == current_year:
        # template is in deze week aangemaakt dus moet niet gekopieerd worden bij permanente aanpassing
        template.trash_containers.remove(to_remove)
        return Response({"message": "Afval container succesvol verwijderd."})

    # neem copy
    copy = make_copy(template, permanent, current_year, current_week)

    # verwijder de oude trashcontainer
    copy.trash_containers.remove(to_remove)

    return Response({"message": "Afval container succesvol verwijderd."})


