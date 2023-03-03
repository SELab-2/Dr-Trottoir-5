from django.db import models


class Manual(models.Model):
    file = models.FileField(upload_to='manuals/')
    fileType = models.TextField()

    # TODO custom of gewoon text based in api
    status = models.TextField()
