from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from string import ascii_uppercase
from .forms import ConverterForm
from .models import FileConverter
from django.views.generic.edit import CreateView
from django.conf import settings
from django.http import HttpResponse, Http404
import csv
import xlsxwriter as xlsx
import os
import mimetypes
from django.http.response import HttpResponse
# Create your views here.

# # Function for storing files
def store_file(file):
    with open("temp/file.csv", "wb+") as destination:
        for chunk in file.chunks():
              destination.write(chunk)

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
            file = request.FILES["user_file"]
            store_file(file)
            ConvertToXLSX(file)
            return HttpResponseRedirect("download file")
        return render(request, "converter/converter.html", {
            "form": submitted_form
        })

def index(request):
    return render(request, "converter/index.html")

class DownloadView(View):
    def get(self, request):
        return render(request, "converter/filedownload.html")

class alpabet():
    excel_alphabet = []
    def generate_excel_alphabet():
        excel_alphabet = [ascii_uppercase[i] for i in range(len(ascii_uppercase))]
        for i in range(26 + 1):
            if(i == 0):
                continue
        for j in range(26):
            excel_alphabet.append(excel_alphabet[i - 1] + excel_alphabet[j])
        return excel_alphabet

def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.abspath(__name__))
    # Define text file name
    filename = 'table(2) (converted).xlsx'
    # Define the full file path
    filepath = BASE_DIR + f"\\download\\{filename}"
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def ConvertToXLSX(file: str):
    print(file)
    file_str = str(file)
    picked_filename_without_file_extension = file_str.replace(".csv", "")
    # Pick save location
    BASE_DIR = os.path.dirname(os.path.abspath(__name__))
    save_location = BASE_DIR + "\\download"
    filepath = BASE_DIR + "\\temp\\file.csv"
    # Workbook() takes one, non-optional, argument
    # which is the filename that we want to create.
    workbook = xlsx.Workbook(
        f"{save_location}/{picked_filename_without_file_extension} (converted).xlsx")
    # The workbook object is then used to add new worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()
    cell_format_currency = workbook.add_format()
    cell_format_number = workbook.add_format()
    cell_format_number.set_num_format('0')
    cell_format_currency.set_num_format('€#,##0.00')
    with open(filepath, newline="") as your_csv_file:
        reader = csv.reader(your_csv_file)
        data = []
        keys = []
        column_length = []
        for row in enumerate(reader):
            column_length = [0] * len(row[1])
            break
        alphabet = alpabet.generate_excel_alphabet()
    with open(filepath, newline="") as your_csv_file:
        reader = csv.reader(your_csv_file)
        for idx, row in enumerate(reader):
            for i in range(len(row)):
                string_row = str(row[i])
                if(column_length[i] < len(string_row)):
                    column_length[i] = len(string_row)
    with open(filepath, newline="") as your_csv_file:
        reader = csv.reader(your_csv_file)
        for idx, row in enumerate(reader):
            if(idx == 0):
                attributes = row
                for i in range(len(attributes)):
                    worksheet.write(f"{alphabet[i]}{idx + 1}", attributes[i])
            else:
                for i in range(len(row)):
                    try:
                        if(attributes[i] == "charge" or attributes[i] == "cogs" or attributes[i] == "net"):
                            row[i] = row[i].replace(",", ".")
                            row[i] = float(row[i])
                            worksheet.write(
                                f"{alphabet[i]}{idx + 1}", row[i], cell_format_currency)
                        else:
                            row[i] = int(row[i])
                            worksheet.write(
                                f"{alphabet[i]}{idx + 1}", row[i], cell_format_number)
                    except:
                        worksheet.write(f"{alphabet[i]}{idx + 1}", row[i])
            for i in range(len(column_length)):
                worksheet.set_column(i,idx, column_length[i])
    workbook.close()