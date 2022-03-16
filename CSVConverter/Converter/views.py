from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

class UploadFileView(View):
    def get(self, request):
        return render(request, "converter/converter.html")
    def post(self, request):
        print(request.FILES["csv"])
        return HttpResponseRedirect("csv-to-xlsx")


def index(request):
    return render(request, "converter/index.html")
