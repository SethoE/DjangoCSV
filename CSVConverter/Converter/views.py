from django.shortcuts import render
from django.views import View
from .forms import ConverterForm
from .models import FileConverter
from django.views.generic.edit import CreateView
# Create your views here.

# Function for storing files
# def store_file(file):
#     with open("temp/file.csv", "wb+") as destination:
#         for chunk in file.chunks():
#               destination.write(chunk)

# class CreateConverterView(CreateView):
#     template_name = "converter/converter.html"
#     model = FileConverter
#     fields = "__all__"
#     success_url = "/download file"
class UploadFileView(View):
    def get(self, request):
        form = ConverterForm()
        return render(request, "converter/converter.html", {
            "form": form
        })
    def post(self, request):
        submitted_form = ConverterForm(request.POST, request.FILES)
        if(submitted_form.is_valid):
            file = FileConverter(file=request.FILES["user_file"])
            file.save()
            print(f"Your file: {request.FILES['user_file']}")
        return render(request, "converter/converter.html", {
            "form": submitted_form
        })


def index(request):
    return render(request, "converter/index.html")

class DownloadView(View):
    def get(self, request):
        return render(request, "converter/filedownload.html")
