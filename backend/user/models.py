from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
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
    email = models.EmailField(_("email"), unique=True)
    name = models.TextField()
    phone_nr = models.TextField()
    access_rights = models.PositiveSmallIntegerField(choices=access_rights_choices, default=1)
    location = None  # Add LocatieEnum model foreign key

    """
        Basic user variables
    """
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    """
        Our custom user has a custom manger for creating the objects.
    """
    objects = CustomUserManager()

    """
        Method that returns the access_rights of a user.
    """
    def get_access_rights(self):
        return self.access_rights
