from .serializers import *
from trashtemplates.models import Status, TrashContainerTemplate
from pickupdays.models import WeekDayEnum, PickUpDay
import datetime


def filter_templates(templates):
    """
    Filter een lijst van templates.
    Als een template eenmalig is aangemaakt in de vorige week dan moet die nu verwijderd worden.
    Ook de template die dan tijdelijk vervangen was moet nu terug toegevoegd worden en op actief gezet worden.

    Hierna blijven dus alleen maar de templates over die actief zijn of in de huidige week eenmalig of vervangen zijn.
    """
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
    return result


def get_current_week_planning():
    """
    Geef de huidige week planning als die bestaat.
    Anders maak je die aan door al de actieve templates toe te voegen en alleen de
    even/oneven bij te houden.
    """
    current_year, current_week, _ = datetime.datetime.utcnow().isocalendar()

    planning, created = WeekPlanning.objects.get_or_create(
        week=current_week,
        year=current_year
    )
    if not created:
        return planning

    # planning bestaat nog niet
    even = current_year % 2 == 0

    # bij filter_templates wordt alles nu normaal omgezet naar actief of verwijderd
    trash_templates = filter_templates(TrashContainerTemplate.objects.all()).filter(even=even)
    student_templates = filter_templates(StudentTemplate.objects.all()).filter(even=even)
    planning.trash_templates.set(trash_templates)
    planning.student_templates.set(student_templates)
    return planning


def make_dag_planning(day, start_hour, end_hour, ronde, students):
    """
    Maakt een nieuwe DagPlanning aan.
    """
    pickup_day, _ = PickUpDay.objects.get_or_create(
        day=day,
        start_hour=start_hour,
        end_hour=end_hour
    )
    dag_planning, _ = DagPlanning.objects.get_or_create(
        ronde_id=ronde,
        time=pickup_day
    )
    dag_planning.students.set(students)
    return dag_planning



def make_copy(template, permanent, current_year, current_week):
    """
        Neemt een copy van een StudentTemplate zodat de geschiedenis behouden wordt
    """

    copy = StudentTemplate.objects.create(
        name=template.name,
        even=template.even,
        status=Status.ACTIEF if permanent else Status.EENMALIG,
        start_hour=template.start_hour,
        end_hour=template.end_hour,
        location=template.location,
        year=current_year,
        week=current_week
    )
    copy.rondes.set(template.rondes.all())
    copy.dag_planningen.set(template.dag_planningen.all())

    # verander de status van de nu oude template
    template.status = Status.INACTIEF if permanent else Status.VERVANGEN
    template.week = current_week
    template.save()

    return copy


def delete_old_dag_planning(old_dag_planningen, day, template):
    """
    Verwijderd de oude DagPlanning van een gegeven dag uit een StudentTemplate
    """
    for old_dag_planning in old_dag_planningen:
        if old_dag_planning.time.day == day:
            template.dag_planningen.remove(old_dag_planning)
            break