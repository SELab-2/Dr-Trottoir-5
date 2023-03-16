from django.db import models


# Create your models here.

class MailTemplate(models.Model):
    name: models.TextField(default="")
    content: models.TextField(default="")

