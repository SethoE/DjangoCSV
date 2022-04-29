from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import User

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "authentication/login.html")

class Register(View):
    def get(self, request):
        return render(request, "authentication/register.html")

    def post(self, request):
        new_user = User()
        register_form_dic = {
            "email": request.POST.get('email'),
            "password": request.POST.get('password'),
            "passwordRepeated": request.POST.get('passwordRepeat'),
            "socialTitle": request.POST.get('socTitle'),
            "firstName": request.POST.get('firstName'),
            "lastName": request.POST.get('lastName')
        }
        if(len(register_form_dic["password"]) >= 8 and register_form_dic["password"] == register_form_dic["passwordRepeated"]):
            new_user.create_new_user(
                register_form_dic["firstName"],
                register_form_dic["lastName"],
                register_form_dic["email"],
                register_form_dic["socialTitle"],
                register_form_dic["password"])

        return render(request, "authentication/register.html")


class Logout(View):
    def get(self, request):
        return render(request, "authentication/logout.html")