from django.db import models
from django.conf import settings
from ronde.models import Ronde


class WeekPlanning(models.Model):
    """
    All the day plans for a certain week

    Attributes
    ----------
    week : models.IntegerField
        The week of the year for this planning

    year : models.IntegerField
        The year of this planning
    """
    week = models.IntegerField()

    year = models.IntegerField()


class DagPlanning(models.Model):
    """
    The planning for 1 student for 1 day

    Attributes
    ----------
    student : models.OneToOneField
        The student that will be doing this round

    date : models.DateField
        The date on which this student will do this round

    ronde : models.ForeignKey
        The round that the student will do this day

    weekPlanning : models.ForeignKey
        WeekPlanning object of which it's a member
    """
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    date = models.DateField()

    ronde = models.ForeignKey(
        Ronde,
        on_delete=models.DO_NOTHING
    )

    weekPlanning = models.ForeignKey(WeekPlanning, on_delete=models.DO_NOTHING)


class InfoPerBuilding(models.Model):
    """
    Info about a building in a round database model.

    Attributes
    ----------
    remark : models.TextField
        The remarks about the building
    dagPlanning: models.ForeignKey
        DagPlanning of which it is an InfoPerBuilding object
    """

    remark = models.TextField(default="")

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
    pictureType: models.CharField
        type of picture. Choices from PictureEnum
    infoPerBuilding: models.ForeignKey
        Reference to the InfoPerBuilding object of which it is an image
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
