from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from ronde.models import LocatieEnum

import random
import string


class Roles(models.TextChoices):
    """
          All the roles users can have.
    """
    ADMIN = "AD", "Admin"
    SUPERSTUDENT = "SU", "Superstudent"
    STUDENT = "ST", "Student"
    SYNDICUS = "SY", "Syndicus"
    BEWONER = "BE", "Bewoner"
    AANVRAGER = "AA", "Aanvrager"


class RoleAssignment(models.Model):
    """
        Model that is used to serialize a role assignment.
    """

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default="AA"
    )


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_nr, password):

        user = self.model(
            email=self.normalize_email(email),
            username=email,
            first_name=first_name,
            last_name=last_name,
            phone_nr=phone_nr
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **args):
        user = self.create_user(**args, first_name='admin', last_name='admin', phone_nr='')
        user.role = 'AD'
        user.save()
        return user


class User(AbstractUser):
    """
        Custom user model.

        Attributes
        ----------

        email: models.EmailField
            Email of the user.

        first_name: models.TextField
            First name of user.

        last_name: models.TextField
            Last name of user

        phone_nr: models.TextField
            Phone number of user

        role: models.CharField
            The role of the user e.g. Admin, Student,...

        otp: models.CharField
            A one time password that is used when a user forgets his password.

        TODO location (ManyToMany)field for Students to know at which location they work

        TODO building (ManyToMany)field for Bewoners/Syndicus to know which buildings they're related to
    """

    email = models.EmailField(verbose_name='email', unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    phone_nr = models.TextField()

    role = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default='AA'
    )

    otp = models.CharField(
        max_length=25,
        default=""
    )
    locations = models.ManyToManyField(LocatieEnum)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        """
            Create new otp when user is saved
        """
        self.otp = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(25))
        super().save(*args, **kwargs)
