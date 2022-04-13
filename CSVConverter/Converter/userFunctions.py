from models import User

class userFunctions():

    def checkIfUserExists(userID):
        try:
            user = User.objects.get(userID=userID)
            return user
        except:
             return False