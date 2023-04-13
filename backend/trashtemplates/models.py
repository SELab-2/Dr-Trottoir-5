from django.db import models
from ronde.models import Building, LocatieEnum
from trashcontainers.models import TrashContainer


class ExtraId(models.Model):
    """
        Een model dat alleen maar een extra ID is.
        Het moet een model zijn zodat er in BuildingTrashContainerList een ManyToManyField gebruikt kan worden.
    """

    id = models.BigAutoField(primary_key=True)


class BuildingTrashContainerList(models.Model):
    """
        Bestaat uit een building en een lijst van ExtraId's.
        Door deze lijst van ExtraId's kunnen we adhv TrashContainerIdWrapper's TrashContainer objecten aanpassen door een nieuw
        TrashContainer object aan te maken waardoor de geschiedenis behouden wordt maar blijft de mapping op dit nu nieuw aangepaste
        object bestaan doordat het ExtraId hier en in TrashContainerIdWrapper hetzelfde blijft.

        Attributes
        ----------
        building : models.ForeignKey(Building)
            Een gebouw

        trash_ids : models.ManyToManyField(ExtraId)
            De geselcteerde trashcontainers van de template waar dit gebouw bijhoort
    """

    building = models.ForeignKey(Building, on_delete=models.DO_NOTHING)
    trash_ids = models.ManyToManyField(ExtraId)


class TrashContainerIdWrapper(models.Model):
    """
        Dit model bestaat uit een ExtraId en een TrashContainer.
        Zoals in BuildingTrashContainerList uitgelegd kan hierdoor dus de geschiedenis en de mapping blijven bestaan.

        Attributes
        ----------
        extra_id : models.ForeignKey(ExtraId)
            Het extra ID zodat de geschiedenis en mapping kan worden behouden.

        trash_container : models.ForeignKey(TrashContainer)
            De trashcontainer zelf
    """

    extra_id = models.ForeignKey(ExtraId, on_delete=models.DO_NOTHING)
    trash_container = models.ForeignKey(TrashContainer, on_delete=models.DO_NOTHING)


class Status(models.TextChoices):
    """
        Enum for the status of templates
    """
    EENMALIG = "E", "Eenmalig"
    VERVANGEN = "V", "Vervangen"
    ACTIEF = "A", "Actief"
    INACTIEF = "I", "Inactief"



class TrashContainerTemplate(models.Model):
    """
        Template die ervoor zorgt dat gebouwen vaste trashcontainers hebben elke week.

        Attributes
        ----------
        name : models.TextField
            Naam van de template.

        even : models.BooleanField
            Bepaalt of de template voor even of oneven weken is.

        location : models.ForeignKey
            De locatie van de template

        status : models.CharField
            Geeft de status van een template aan

        year : models.IntegerField
            Geeft het jaar aan waarin de template gemaakt is.

        week : models.IntegerField
            Geeft de week aan waarin de template gemaakt is.

        buildings : models.ManyToManyField(BuildingTrashContainerList)
            De lijst met gebouwen die deze template gebruiken en hun geselecteerde trashcontainers.

        trash_containers : models.ManyToManyField(TrashContainerIdWrapper)
            Lijst van alle trashcontainers in deze template.

    """
    def __getitem__(self, item):
        if item == "buildings":
            return self.buildings
        if item == "trash_containers":
            return self.trash_containers

    name = models.TextField()
    even = models.BooleanField()
    location = models.ForeignKey(LocatieEnum, on_delete=models.DO_NOTHING)
    status = models.CharField(
        max_length=1,
        choices=Status.choices
    )
    year = models.IntegerField()
    week = models.IntegerField()
    buildings = models.ManyToManyField(BuildingTrashContainerList, blank=True)
    trash_containers = models.ManyToManyField(TrashContainerIdWrapper, blank=True)
