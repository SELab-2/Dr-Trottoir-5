from django.db import models
from django_postgres_extensions.models.fields import ArrayField
from LocatieEnum import LocatieEnum
from Building import Building


class Ronde(models.Model):
    naam = models.TextField()
    locatie = models.ForeignKey(
        LocatieEnum,
        on_delete=models.DO_NOTHING,
        verbose_name="Locatie"
    )
    buildings = ArrayField(Building)
