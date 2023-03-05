from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class User(AbstractBaseUser):
    """
        Custom User model

    """
    access_rights_choices = (
        (1, 'student'),
        (2, 'super student'),
        (3, 'admin'),
        (4, 'syndicus'),
        (5, 'house owner'),
    )

    name = models.TextField()
    email = models.EmailField()
    phone_nr = models.TextField()
    access_rights = models.PositiveSmallIntegerField(choices=access_rights_choices)
    locatie = None  # Add LocatieEnum model
