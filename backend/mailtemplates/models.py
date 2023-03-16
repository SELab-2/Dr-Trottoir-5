from django.db import models


class MailTemplate(models.Model):
    name = models.TextField(default='')
    content = models.TextField(default='')
