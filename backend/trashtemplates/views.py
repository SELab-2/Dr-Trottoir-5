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

@api_view(["POST"])
@permission_classes([AllowAny])
def perm_add_trash_container(request, template_id):
    data = request.data

    # maak nieuwe pickupday met de aangepaste data
    new_pickup_day, created = PickUpDay.objects.get_or_create(
        day=data["day"],
        start_hour=data["start_hour"],
        end_hour=data["end_hour"]
    )

    # maak nieuwe container met deze aangepaste pickupday
    new_trash_container = TrashContainer.objects.create(
        type=data["type"],
        collection_day=new_pickup_day
    )

    # maak een wrapper met een nieuw extra id en de nieuwe trashcontainer
    new_extra_id = ExtraId.objects.create()
    tc_id_wrapper = TrashContainerIdWrapper.objects.create(
        extra_id=new_extra_id,
        trash_container=new_trash_container
    )

    current_year = datetime.datetime.utcnow().isocalendar()[0]
    current_week = datetime.datetime.utcnow().isocalendar()[1]

    template = TrashContainerTemplate.objects.get(id=template_id)

    if template.week == current_week and template.year == current_year:
        # template is in deze week aangemaakt dus moet niet gekopieerd worden bij een aanpassing
        template.trash_containers.add(tc_id_wrapper)
        return Response({"message": "Afval container succesvol toegevoegd"})

    # verander de status van de nu oude template
    template.status = "verwijderd"
    template.save()

    # neem een copy
    copy = TrashContainerTemplate.objects.create(
        name=template.name,
        even=template.even,
        status="actief",
        year=current_year,
        week=current_week,
        buildings=template.buildings.all(),
        trash_containers=template.trash_containers.all()
    )

    # voeg de nieuwe trashcontainer toe aan de copy
    copy.trash_containers.add(tc_id_wrapper)
    return Response({"message": "Afval container succesvol toegevoegd"})

@api_view(["POST"])
@permission_classes([AllowAny])
def temp_edit_trash_container(request, template_id):
    data = request.data

    current_year = datetime.datetime.utcnow().isocalendar()[0]
    current_week = datetime.datetime.utcnow().isocalendar()[1]

    # verander status van origineel
    template = TrashContainerTemplate.objects.get(id=template_id)
    template.status = "tijdelijk vervangen"
    template.week = current_week
    template.save()

    # neem copy
    copy = TrashContainerTemplate.objects.create(
        name=template.name + " eenamlig",
        even=template.even,
        status="tijdelijk",
        year=current_year,
        week=current_week
    )
    copy.buildings.set(template.buildings.all())
    copy.trash_containers.set(template.trash_containers.all())


    # vind de oude versie van de trashcontainer en verwijder die uit de copy
    extra_id = ExtraId.objects.get(id=data["extra_id"])
    to_remove = copy.trash_containers.get(extra_id=extra_id)
    copy.trash_containers.remove(to_remove)

    # maak nieuwe pickupday met de aangepaste data
    new_pickup_day, created = PickUpDay.objects.get_or_create(
        day=data["day"],
        start_hour=data["start_hour"],
        end_hour=data["end_hour"]
    )
    # maak nieuwe container met deze aangepaste pickupday
    new_trash_container = TrashContainer.objects.create(
        type=data["type"],
        collection_day=new_pickup_day
    )

    # maak een wrapper met de oorspronkelijke extra id en de nieuwe trashcontainer
    tc_id_wrapper = TrashContainerIdWrapper.objects.create(
        extra_id=extra_id,
        trash_container=new_trash_container
    )
    # voeg die toe aan de copy
    copy.trash_containers.add(tc_id_wrapper)

    return Response({"message": "Afval container succesvol aangepast"})

