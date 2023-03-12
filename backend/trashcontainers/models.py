from django.db import models


class Weekday(models.Model):
    """
        Model for the days of the week so it can be used in a ManyToManyField.
    """

    class WeekDayEnum(models.TextChoices):
        """
              Enum for the days of the week.
        """
        MONDAY = "MO", "Monday"
        TUESDAY = "TU", "Tuesday"
        WEDNESDAY = "WE", "Wednesday"
        THURSDAY = "TH", "Thursday"
        FRIDAY = "FR", "Friday"
        SATURDAY = "SA", "Saturday"
        SUNDAY = "SU", "Sunday"

    weekday = models.CharField(
        max_length=2,
        choices=WeekDayEnum.choices
    )


class TrashContainer(models.Model):
    """
        Trash Container database model.

        Attributes
        ----------

        type : models.CharField
            The type of trash that is in the container

        collection_days : models.ManyToManyField
            The days that the container needs to be collected

        special_actions : models.TextField
            The possible special actions that need to be taken

        start_hour : models.TimeField
            The time when they start collecting the trash container

        end_hour: models.TimeField
            The time when they stop collecting the trash container
       """

    class TrashType(models.TextChoices):
        """
            Enum for the types of trash.
        """
        PMD = "PM", "PMD"
        REST = "RE", "REST"
        PK = "PK", "PK"
        GLAS = "GL", "GLAS"
        GFT = "GF", "GFT"

    type = models.CharField(
        max_length=2,
        choices=TrashType.choices
    )

    collection_days = models.ManyToManyField(Weekday)

    special_actions = models.TextField(
        default=""
    )

    start_hour = models.TimeField()
    end_hour = models.TimeField()
