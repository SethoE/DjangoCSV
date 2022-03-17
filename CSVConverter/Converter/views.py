from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

# Function for storing files
def store_file(file):
    with open("temp/file.csv", "wb+") as destination:
        for chunk in file.chunks():
              destination.write(chunk)
class UploadFileView(View):
    def get(self, request):
        return render(request, "converter/converter.html")
    def post(self, request):
        store_file(request.FILES["csv"])
        return HttpResponseRedirect("csv-to-xlsx")


def index(request):
    return render(request, "converter/index.html")
