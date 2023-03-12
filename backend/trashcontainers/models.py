from django.db import models

from pickupdays.models import PickUpDay


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

    collection_days = models.ManyToManyField(PickUpDay)

    special_actions = models.TextField(
        default=""
    )
