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
def trash_container_view(request, template_id):
    data = request.data
    permanent = data["permanent"]
    method = data["method"]  # add, edit of delete

    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    template = TrashContainerTemplate.objects.get(id=template_id)

    # alleen bij add moet er een nieuwe ExtraId aangemaakt worden
    extra_id = ExtraId.objects.create() if method == "add" else ExtraId.objects.get(id=data["extra_id"])

    # alleen bij edit en remove moet er een oude copy verwijderd worden
    to_remove = None if method == "add" else template.trash_containers.get(extra_id=extra_id)

    # alleen bij edit en add moet er een nieuwe TrashContainerIdWrapper gemaakt worden
    tc_id_wrapper = None if method == "delete" else make_new_tc_id_wrapper(data, extra_id)

    if permanent and template.week == current_week and template.year == current_year:
        # template is in deze week aangemaakt dus moet niet gekopieerd worden bij permanente aanpassing
        if to_remove is not None:
            template.trash_containers.remove(to_remove)

        if tc_id_wrapper is not None:
            template.trash_containers.add(tc_id_wrapper)

        return Response({"message": "Success"})

    # neem copy om de geschiedenis te behouden
    copy = make_copy(template, permanent, current_year, current_week)

    if to_remove is not None:
        copy.trash_containers.remove(to_remove)

    if tc_id_wrapper is not None:
        copy.trash_containers.add(tc_id_wrapper)

    return Response({"message": "Success"})
