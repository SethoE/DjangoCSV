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

        return HttpResponseRedirect("sign-in")


class Logout(View):
    def get(self, request):
        return render(request, "authentication/logout.html")