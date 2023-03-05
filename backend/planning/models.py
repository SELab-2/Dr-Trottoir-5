import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class BuildingPicture(models.Model):
    """
    Building Picture database model.

    Attributes
    ----------
    id : UUIDField
        the Identifier of this field

    image : models.ImageField
        the image that is being stored

    time : models.DateTimeField
        The date and time at which the picture was taken

    remark : models.CharField
        The remarks about the picture
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

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
    id : UUIDField
        the Identifier of this field

    arrival : models.ForeignKey
        The images taken when the student arrives on location

    storage : models.ForeignKey
        The images taken when the student is in the storage location

    departure : models.ForeignKey
        The images taken when the student departs

    extra : models.ForeignKey
        Extra images the student has taken

    remark : models.CharField
        The remarks about the building
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    arrival = models.ForeignKey(BuildingPicture, on_delete=models.CASCADE)

    storage = models.ForeignKey(BuildingPicture, on_delete=models.CASCADE)

    departure = models.ForeignKey(BuildingPicture, on_delete=models.CASCADE)

    extra = models.ForeignKey(BuildingPicture, on_delete=models.CASCADE)

    remark = models.CharField(
        default="",
        max_length=500
    )


class DagPlanning(models.Model):
    """
    The planning for 1 student for 1 day

    Attributes
    ----------
    id : UUIDField
        the Identifier of this field

    student : models.OneToOneField
        The student that will be doing this round

    date : models.DateField
        The date on which this student will do this round

    ronde : models.ForeignKey
        The round that the student will do this day

    info : models.ForeignKey
        All the info from the student about all the buildings

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    student = models.OneToOneField(AbstractUser, on_delete=models.DO_NOTHING)

    date = models.DateField  # TODO moet dit DateTimeField worden?

    ronde = None  # TODO

    info = models.ForeignKey(InfoPerBuilding, on_delete=models.CASCADE)


class WeekPlanning(models.Model):
    """
    All the day plans for a certain week

    Attributes
    ----------
    id : UUIDField
        the Identifier of this field

    week : models.IntegerField
        The week of the year for this planning

    year : models.IntegerField
        The year of this planning

    dagPlanningen : models.ForeignKey
        All the DayPlannings for this week

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    week = models.IntegerField

    year = models.IntegerField

    dagPlanningen = models.ForeignKey(DagPlanning, on_delete=models.DO_NOTHING)
