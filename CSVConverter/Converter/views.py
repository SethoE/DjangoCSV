from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "converter/index.html")

def converter(request):
    return render(request, "converter/converter.html")