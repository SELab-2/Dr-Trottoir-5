from pickupdays.models import PickUpDay
from .serializers import *
from trashcontainers.models import TrashContainer


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

