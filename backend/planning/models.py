from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


class BuildingPicture(models.Model):
    """
    Building Picture database model.

    Attributes
    ----------
    image : models.ImageField
        the image that is being stored

    time : models.DateTimeField
        The date and time at which the picture was taken

    remark : models.CharField
        The remarks about the picture
    """
    image = models.ImageField
    time = models.DateTimeField
    remark = models.CharField(
        default="",
        max_length=500
    )


class InfoPerBuilding(models.Model):
    """
    Info about a building in a round database model.

    Attributes
    ----------
    arrival : ArrayField(BuildingPicture)
        The images taken when the student arrives on location

    storage : ArrayField(BuildingPicture)
        The images taken when the student is in the storage location

    departure : ArrayField(BuildingPicture)
        The images taken when the student departs

    extra : ArrayField(BuildingPicture)
        Extra images the student has taken

    remark : models.CharField
        The remarks about the building
    """
    arrival = ArrayField(BuildingPicture)
    storage = ArrayField(BuildingPicture)
    departure = ArrayField(BuildingPicture)
    extra = ArrayField(BuildingPicture)
    remark = models.CharField(
        default="",
        max_length=500
    )


class DagPlanning(models.Model):
    """
    The planning for 1 student for 1 day

    Attributes
    ----------
    student : AbstractUser
        The student that will be doing this round

    date : models.DateField
        The date on which this student will do this round

    ronde : # TODO
        The round that the student will do this day

    info : ArrayField(InfoPerBuilding)
        All the info from the student about all the buildings

    """
    student = AbstractUser

    date = models.DateField  # TODO moet dit DateTimeField worden?

    ronde = None  # TODO

    info = ArrayField(InfoPerBuilding)


class WeekPlanning(models.Model):
    """
    All the day plans for a certain week

    Attributes
    ----------
    week : models.IntegerField
        The week of the year for this planning

    year : models.IntegerField
        The year of this planning

    dagPlanningen : ArrayField(DagPlanning)
        All the DayPlannings for this week

    """
    week = models.IntegerField

    year = models.IntegerField

    dagPlanningen = ArrayField(DagPlanning)
