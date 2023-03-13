from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework import serializers

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Registration(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.TextField(default="")
    last_name = models.TextField(default="")
    password = models.CharField(max_length=30, default=None)

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

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default="AA"
    )


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        if not email:
            raise serializers.ValidationError(
                {
                    "errors": [
                        {
                            "message": "email is required", "field": "email"
                        }
                    ]
                }, code='invalid')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True, primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()

    role = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default='AA'
    )
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
