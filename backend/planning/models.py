from django.db import models
from django.conf import settings
from ronde.models import Ronde
from trashtemplates.models import TrashContainerTemplate, Status
from pickupdays.models import PickUpDay
from ronde.models import LocatieEnum


class DagPlanning(models.Model):
    """
    The planning for one Ronde on a specific day

    Attributes
    ----------
    students : models.ManyToMany
        The students that will be doing this round

    time : models.ForeignKey
        The weekday, start hour and end hour

    ronde : models.ForeignKey
        The round that the students will do this day

    """
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    time = models.ForeignKey(PickUpDay, on_delete=models.DO_NOTHING)

    ronde = models.ForeignKey(
        Ronde,
        on_delete=models.DO_NOTHING
    )


class StudentTemplate(models.Model):
    """
    Studenten template die studenten met rondes matcht.

    Attributes
    ----------
    name : models.TextField
        De naam van deze template

    even : models.BooleanField
        Bepaalt of de template voor even of oneven weken is.

    location : models.ForeignKey
        De locatie van de template.

    status : models.TextField
        Geeft de status van een template aan.

    year : models.IntegerField
        Geeft het jaar aan waarin de template gemaakt is.

    week : models.IntegerField
        Geeft de week aan waarin de template gemaakt is.

    start_hour : models.TimeField
        De standaard tijd wanneer een ronde begint.

    start_hour : models.TimeField
        De standaard tijd wanneer een ronde eindigt.

    rondes : models.ManyToManyField
        Al de rondes die in deze template zitten.

    dag_planningen : models.ManyToManyField
        Al de dagplanningen van deze rondes.

    """
    def __getitem__(self, item):
        if item == "dag_planningen":
            return self.dag_planningen

    name = models.TextField()
    even = models.BooleanField()
    location = models.ForeignKey(LocatieEnum, on_delete=models.DO_NOTHING)

    status = models.CharField(
        max_length=1,
        choices=Status.choices
    )
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    year = models.IntegerField()
    week = models.IntegerField()
    rondes = models.ManyToManyField(Ronde, blank=True)
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
    def __getitem__(self, item):
        if item == "trash_templates":
            return self.trash_templates
        if item == "student_templates":
            return self.student_templates

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
