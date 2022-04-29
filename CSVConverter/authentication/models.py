from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    socialTitle = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    email = models.EmailField()
    is_authenticated = models.BooleanField(default=False)

    def create_new_user(self, firstname: str, lastname:str, email:str, socialTitle:str ,password:str):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def update_existing_user(userID, first_name: str=None, last_name: str=None, password: str=None, email: str=None):
        try:
            specific_user = User.objects.get(userID=userID)
            if(first_name != None):
                specific_user.firstname = first_name
            if(last_name != None):
                specific_user.lastname = last_name
            if(password != None):
                specific_user.password = password
            if(email != None):
                specific_user.email = email
            specific_user.save()
        except:
            pass



    def get_user_data(userID):
        try:
            specific_user = User.objects.get(userID=userID)
        except:
            pass
        return specific_user