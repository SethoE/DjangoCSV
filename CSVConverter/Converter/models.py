from django.db import models
from  django.core.validators import MinValueValidator, MaxLengthValidator
from authentication.models import User
import os

# Create your models here.

class FileConverter(models.Model):
    file = models.FileField(upload_to="CSV")

    # def filename(self):
    #     return os.path.basename(self.file.name)
class File(models.Model):
    fileID = models.AutoField(primary_key=True)
    uploadDate = models.DateField()
    filename = models.CharField(max_length=100)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)







