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
        for i in register_form_dic:
            print(f"{i}: {register_form_dic[i]}")

        return render(request, "authentication/register.html")


class Logout(View):
    def get(self, request):
        return render(request, "authentication/logout.html")