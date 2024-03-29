from pickupdays.models import PickUpDay
from .serializers import *
from trashcontainers.models import TrashContainer
from ronde.models import Building
from planning.util import get_current_time
from exceptions.exceptionHandler import ExceptionHandler

from pickupdays.models import WeekDayEnum


def get_trash_template(template_id):
    handler = ExceptionHandler()
    handler.check_primary_key(template_id, "template_id", TrashContainerTemplate)
    handler.check()
    template = TrashContainerTemplate.objects.get(id=template_id)
    handler.check_not_inactive(template, "template")
    handler.check()
    return template


def make_new_tc_id_wrapper(data, extra_id):
    """
        Maakt nieuwe TrashContainerIdWrapper aan.
    """
    handler = ExceptionHandler()
    handler.check_time_value_required(data.get("collection_day").get("start_hour"), "start_hour")
    handler.check_time_value_required(data.get("collection_day").get("end_hour"), "end_hour")
    handler.check_enum_value_required(data.get("collection_day").get("day"), "day", WeekDayEnum)
    handler.check_enum_value_required(data.get("type"), "type", TrashContainer.TrashType)
    handler.check()

    # maak nieuwe pickupday met de aangepaste data
    new_pickup_day, _ = PickUpDay.objects.get_or_create(
        day=data["collection_day"]["day"],
        start_hour=data["collection_day"]["start_hour"],
        end_hour=data["collection_day"]["end_hour"]
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


def make_new_building_list(building_id, selection):
    """
        Maakt nieuwe BuildingTrashContainerList aan.
        TODO checks
    """
    building = Building.objects.get(id=building_id)
    new_building_list = BuildingTrashContainerList.objects.create(
        building=building
    )
    new_building_list.trash_ids.set(selection)
    return new_building_list


def make_copy(template, permanent, current_year, current_week):
    """
        Neemt een copy van een template zodat de geschiedenis behouden wordt
        Als er een oneven template wordt aangepast in een even week zijn deze aanpassingen pas voor
        de volgende week.
    """
    week = current_week
    if (current_week % 2 == 0) != template.even:
        week += 1

    copy = TrashContainerTemplate.objects.create(
        name=template.name,
        even=template.even,
        status=Status.ACTIEF if permanent else Status.EENMALIG,
        location=template.location,
        year=current_year,
        week=week
    )
    copy.buildings.set(template.buildings.all())
    copy.trash_containers.set(template.trash_containers.all())

    # verander de status van de nu oude template
    template.status = Status.INACTIEF if permanent else Status.VERVANGEN
    template.week = week
    template.save()

    return copy


def no_copy(template, permanent, current_year, current_week):
    """
    Controleert of een template gekopieerd moet worden.

    Wanneer de template eenmalig is moet deze niet gekopieerd worden.
    Ook wanneer het een permanente aanpassing is op een actieve template die deze week is aangemaakt moet er
    niks gekopieerd worden.
    """
    return template.status == Status.EENMALIG or (
        permanent and template.week == current_week and template.year == current_year)


def add_if_match(many_to_many, new_template, current_week):
    """
    Voeg de niewe template alleen maar toe als even/oneven matcht en hij er nog niet inzit.
    """
    if new_template.even == (current_week % 2 == 0) and not many_to_many.filter(id=new_template.id).exists():
        many_to_many.add(new_template)


def remove_if_match(many_to_many, old_template):
    """
    Verwijder de oude template alleen maar als hij in de many_to_many zat.
    """
    if many_to_many.filter(id=old_template.id).exists():
        many_to_many.remove(old_template)


def update_many_to_many(template, many_to_many, old, new):
    """
    Past een many_to_many veld aan.

    @param template: De originele template
    @param many_to_many: Het veld dat aangepast wordt van de template
    @param old: De oude waarde
    @param new: De nieuwe waarde
    """
    # verwijder de oude
    if old is not None:
        template[many_to_many].remove(old)
    # voeg de nieuwe toe
    if new is not None:
        template[many_to_many].add(new)


def update(template, many_to_many, old, new, permanent, template_list, copy_template=make_copy):
    """
    Past het betreffende many_to_many veld van de template aan.
    Als het nodig is wordt er ook een copy gemaakt van de template zodat de geschiedenis behouden wordt.

    @param copy_template: Functie die een template kopieert
    @param template: De originele template
    @param many_to_many: Het veld dat aangepast wordt van de template
    @param old: De oude waarde
    @param new: De nieuwe waarde
    @param permanent: Of de aanpassing permanent is
    @param template_list: De lijst van alle templates van de huidige weekplanning
    """
    current_year, current_week = get_current_time()
    if no_copy(template, permanent, current_year, current_week):
        update_many_to_many(template, many_to_many, old, new)
        return {"message": "success"}
    else:
        copy = copy_template(template, permanent, current_year, current_week)
        update_many_to_many(copy, many_to_many, old, new)
        remove_if_match(template_list, template)
        add_if_match(template_list, copy, current_week)
        return {
            "message": "success",
            "new_id": copy.id
        }
