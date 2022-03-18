from django.db import models
import os

# Create your models here.

class FileConverter(models.Model):
    file = models.FileField(upload_to="CSV")

    def filename(self):
        return os.path.basename(self.file.name)