from django.db import models


class PickUpDay(models.Model):
    """
        The pickup day and hours for a TrashContainer.
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

    day = models.CharField(
        max_length=2,
        choices=WeekDayEnum.choices
    )

    start_hour = models.TimeField()
    end_hour = models.TimeField()
