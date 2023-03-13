from django.db import models


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
    student = None  # TODO # models.OneToOneField(AbstractUser, on_delete=models.DO_NOTHING)

    date = models.DateField()

    ronde = None  # TODO

    weekPlanning = models.ForeignKey(WeekPlanning, on_delete=models.DO_NOTHING)


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
