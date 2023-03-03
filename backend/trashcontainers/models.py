from django.db import models
from django.contrib.postgres.fields import ArrayField

class TrashContainer(models.Model):
    class TrashType(models.TextChoices):
        PMD = "PM", "PMD"
        REST = "RE", "REST"
        PK = "PK", "PK"
        GLAS = "GL", "GLAS"
        GFT = "GF", "GFT"

    class WeekDay(models.TextChoices):
        MONDAY = "MO", "Monday"
        TUESDAY = "TU", "Tuesday"
        WEDNESDAY = "WE", "Wednesday"
        THURSDAY = "TH", "Thursday"
        FRIDAY = "FR", "Friday"
        SATURDAY = "SA", "Saturday"
        SUNDAY = "SU", "Sunday"


    type = models.CharField(
        max_length=2,
        choices=TrashType.choices
    )

    collection_days = ArrayField(
        models.CharField(
            max_length=2,
            choices=WeekDay.choices
        )
    )
    special_actions = models.CharField(
        default="",
        max_length=500
    )

    start_hour = models.TimeField()
    end_hour = models.TimeField()