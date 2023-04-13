from django.db import models
from django.conf import settings
import uuid


class LocatieEnum(models.Model):
    """
            LocatieEnum database model.
            Attributes
            ----------
            name : models.TextField
                The name of a location.
    """
    name = models.TextField()


class ManualStatusField(models.TextChoices):
    """
          Custom textfield for the status of a manual.
    """

    klaar = "Klaar"
    update_nodig = "Update nodig"
    bezig = "Bezig"
    geupdatet = "Geüpdatet"


class Manual(models.Model):
    """
            Manual database model.
            Attributes
            ----------
            file : models.FileField
                The file of the manual. It's saved with as root the MEDIA_URL of settings.py.
            fileType : models.TextField
                The type of the Manual file.
            manualStatus : ManualStatusField
                The status of the manual for a building.
    """

    #    Method for creating upload path
    def upload_to(self, filename):
        return f'manuals/{filename}'

    file = models.FileField(upload_to=upload_to)
    fileType = models.TextField()
    manualStatus = models.TextField(choices=ManualStatusField.choices)


class Building(models.Model):
    """
            Building database model.
            Attributes
            ----------
            adres : models.Textfield
                The adres of a building
            syndicus : models.TextField
                The owner of a building.
            owners : models.ManyToManyField
                The people that live in a building.
            ivago_klantnr : models.IntegerField
                The ivago klantnummer of a building.
            manual : ForeignKey
                The manual of a building.
            containers : ForeignKey
                The trash containers a building has.
            locatie : LocatieEnum
                The location of a building.
            special_actions : models.TextField
                The possible special actions that need to be taken
            buildingID: UUID
                unique identifier of a building to add people
    """
    adres = models.TextField()
    syndicus = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    ),
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL),
    ivago_klantnr = models.IntegerField()
    manual = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE, blank=True, null=True
    )
    location = models.ForeignKey(
        LocatieEnum,
        on_delete=models.DO_NOTHING
    )
    special_actions = models.TextField(
        default="",
        blank=True
    )
    # default uuid.uuid4 is callable en genereerd uuid
    buildingID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


class Ronde(models.Model):
    """
         Ronde database model.
         Attributes
         ----------
         name : models.Textfield
             The name of the ronde
         locatie : ForeignKey
             The location of the ronde
         building : models.ManyToManyField
             The different buildings that need te be visited in a ronde
    """

    name = models.TextField()
    location = models.ForeignKey(
        LocatieEnum,
        on_delete=models.DO_NOTHING,
        verbose_name="Locatie"
    )
    buildings = models.ManyToManyField(Building, blank=True)
