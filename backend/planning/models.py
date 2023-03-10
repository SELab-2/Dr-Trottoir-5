from django.db import models
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

    remark : models.TextField
        The remarks about the picture
    """
    image = models.ImageField()

    time = models.DateTimeField()

    remark = models.TextField(default="")


class InfoPerBuilding(models.Model):
    """
    Info about a building in a round database model.

    Attributes
    ----------
    arrival : models.ForeignKey
        The images taken when the student arrives on location

    storage : models.ForeignKey
        The images taken when the student is in the storage location

    departure : models.ForeignKey
        The images taken when the student departs

    extra : models.ForeignKey
        Extra images the student has taken

    remark : models.TextField
        The remarks about the building
    """
    arrival = models.ForeignKey(BuildingPicture, on_delete=models.CASCADE, related_name="arrival")

    storage = models.ForeignKey(BuildingPicture, on_delete=models.CASCADE, related_name="storage")

    departure = models.ForeignKey(BuildingPicture, on_delete=models.CASCADE, related_name="departure")

    extra = models.ForeignKey(BuildingPicture, on_delete=models.CASCADE, related_name="extra")

    remark = models.TextField(default="")


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

    info : models.ForeignKey
        All the info from the student about all the buildings

    """
    student = None # models.OneToOneField(AbstractUser, on_delete=models.DO_NOTHING)

    date = models.DateField()

    ronde = None  # TODO

    info = models.ForeignKey(InfoPerBuilding, on_delete=models.CASCADE)


class WeekPlanning(models.Model):
    """
    All the day plans for a certain week

    Attributes
    ----------
    week : models.IntegerField
        The week of the year for this planning

    year : models.IntegerField
        The year of this planning

    dagPlanningen : models.ForeignKey
        All the DayPlannings for this week

    """
    week = models.IntegerField()

    year = models.IntegerField()

    dagPlanningen = models.ForeignKey(DagPlanning, on_delete=models.DO_NOTHING)
