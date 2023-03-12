from django.db import models
from trashcontainers.models import TrashContainer


class User(models.Model):
    """
        TODO
        Temporal model of user
    """
    name = models.TextField()


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

    file = models.FileField(upload_to='manuals/')
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
    """
    adres = models.TextField()
    syndicus = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    ),
    owners = models.ManyToManyField(User),
    ivago_klantnr = models.IntegerField()
    manual = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE
    )
    containers = models.ForeignKey(
        TrashContainer,
        on_delete=models.DO_NOTHING
    )
    location = models.ForeignKey(
        LocatieEnum,
        on_delete=models.DO_NOTHING
    )


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
    buildings = models.ManyToManyField(Building)