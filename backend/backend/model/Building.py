from django.db import models
from User import User
from Manual import Manual
from LocatieEnum import LocatieEnum


class Building(models.Model):
    adres = models.TextField()
    syndicus = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    ),
    owners = ArrayField(User),
    ivago_klantnr = models.IntegerField()
    manual = models.ForeignKey(
        Manual,
        on_delete=models.CASCADE
    )
    # TODO Add TrashContainer model
    # containers = ArrayField(TrashContainers)
    locatie = models.ForeignKey(
        LocatieEnum,
        on_delete=models.DO_NOTHING
    )
