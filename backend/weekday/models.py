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

