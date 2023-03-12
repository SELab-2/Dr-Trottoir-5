from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Registration(models.Model):
    email = models.EmailField(unique=True)
    name = models.TextField()
    password = models.CharField(max_length=30, default=None)



class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError()

        user = self.model(
            email=self.normalize_email(email),
            username=name
        )
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True)
    name = models.TextField()

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
