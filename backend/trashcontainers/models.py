from django.db import models
from pickupdays.models import PickUpDay


class TrashContainer(models.Model):
    """
        Trash Container database model.

        Attributes
        ----------

        type : models.CharField
            The type of trash that is in the container

        collection_day : models.ManyToManyField
            The days that the container needs to be collected

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

    collection_day = models.ForeignKey(PickUpDay, on_delete=models.DO_NOTHING)

