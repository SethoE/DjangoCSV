from django.db import models

# Create your models here.

class FileConverter(models.Model):
    file = models.FileField(upload_to="CSV")