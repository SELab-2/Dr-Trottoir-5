from django.db import models
from django.conf import settings
from ronde.models import Ronde
from trashtemplates.models import TrashContainerTemplate
from pickupdays.models import PickUpDay


class DagPlanning(models.Model):
    """
    The planning for one Ronde on a specific day

    Attributes
    ----------
    students : models.ManyToMany
        The students that will be doing this round

    date : models.ForeignKey
        The date on which this student will do this round.
        Only the weekday is stored so the object can be reused in templates.

    ronde : models.ForeignKey
        The round that the students will do this day

    """
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    date = models.ForeignKey(PickUpDay, on_delete=models.DO_NOTHING)

    ronde = models.ForeignKey(
        Ronde,
        on_delete=models.DO_NOTHING
    )


class StudentTemplate(models.Model):
    """
    All the day templates for a certain week

    Attributes
    ----------
    name : models.TextField
        The name of this template

    status : models.TextField
        Geeft de status van een template aan: actief/tijdelijk/verwijderd/tijdelijk vervangen

    year : models.IntegerField
        Geeft het jaar aan waarin de template gemaakt is.

    week : models.IntegerField
        Geeft de week aan waarin de template gemaakt is.

    dag_planningen : models.ManyToManyField
        The DagPlanning objects of this template

    """
    name = models.TextField()
    status = models.TextField()  # TODO choicefield
    year = models.IntegerField()
    week = models.IntegerField()
    dag_planningen = models.ManyToManyField(DagPlanning, blank=True)



class WeekPlanning(models.Model):
    """
    All the day templates for a certain week

    Attributes
    ----------
    week : models.IntegerField
        The week of the year for this planning

    year : models.IntegerField
        The year of this planning

    trash_templates: models.ManyToManyField(TrashContainerTemplate)
        The trash templates for this week

    student_templates: models.ManyToManyField(StudentTemplate)
        The student templates for this week

    """
    week = models.IntegerField()

    year = models.IntegerField()

    trash_templates = models.ManyToManyField(TrashContainerTemplate, blank=True)
    student_templates = models.ManyToManyField(StudentTemplate, blank=True)


class InfoPerBuilding(models.Model):
    """
    Info about a building in a round database model.

    Attributes
    ----------
    remark : models.TextField
        The remarks about the building

    date : models.DateField
        The date when this info was created.
        Because of this we can reuse DagPlanning objects.

    dagPlanning : models.ForeignKey
        The associated DagPlanning
    """

    remark = models.TextField(default="")

    date = models.DateField()

    dagPlanning = models.ForeignKey(DagPlanning, on_delete=models.CASCADE)


class BuildingPicture(models.Model):
    """
    Building Picture database model.

    Attributes
    ----------
    image : models.ImageField
        the image that is being stored

    time : models.DateTimeField
        The date and time at which the picture was taken

    remark : models.TextField
        The remarks about the picture
    """

    class PictureEnum(models.TextChoices):
        """
        enum for type of picture
        """
        ARRIVAL = "AR", "Arrival"
        STORAGE = "ST", "Storage"
        DEPARTURE = "DE", "Departure"
        EXTRA = "EX", "Extra"

    pictureType = models.CharField(
        max_length=2,
        choices=PictureEnum.choices
    )

    image = models.ImageField()

    time = models.DateTimeField()

    remark = models.TextField(default="")

    infoPerBuilding = models.ForeignKey(InfoPerBuilding, on_delete=models.CASCADE)
