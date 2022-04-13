from django.db import models
from  django.core.validators import MinValueValidator, MaxLengthValidator
from userFunctions import userFunctions
import os

# Create your models here.

class FileConverter(models.Model):
    file = models.FileField(upload_to="CSV")

    # def filename(self):
    #     return os.path.basename(self.file.name)

class User(models.Model):
    userID = models.AutoField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    email = models.EmailField()

    def create_new_user(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def update_existing_user(self, userID, first_name: str=None, last_name: str=None, password: str=None, email: str=None):
        specific_user = userFunctions.checkIfUserExists(userID=userID)
        if(first_name != None):
            self.firstname = first_name
        if(first_name != None):
            self.lastname = last_name
        if(first_name != None):
            self.password = password
        if(first_name != None):
            self.email = email

    def get_user_data(userID):
        specific_user = userFunctions.checkIfUserExists(userID=userID)
        return specific_user

class File(models.Model):
    fileID = models.AutoField()
    uploadDate = models.DateField()
    filename = models.CharField(max_length=100)

    userID = models.ForeignKey(User, on_delete=models.CASCADE)







