from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from string import ascii_uppercase
from .forms import ConverterForm
from django.http import HttpResponse
import csv
import xlsxwriter as xlsx
import os
import mimetypes
from django.http.response import HttpResponse


def store_file(file):
    BASE_DIR = os.path.dirname(os.path.abspath(__name__))
    filepath = BASE_DIR + f"\\temp\\{file}"
    with open(filepath, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class UploadFileView(View):
    def get(self, request):
        form = ConverterForm()
        return render(request, "converter/converter.html", {
            "form": form
        })

    def post(self, request):
        submitted_form = ConverterForm(request.POST, request.FILES)
        if(submitted_form.is_valid):
            uploaded_file_name = request.FILES["user_file"]
            store_file(uploaded_file_name)
            converted_file = ConvertToXLSX(uploaded_file_name)
            if(converted_file == "NULL"):
                return HttpResponseRedirect("file error")
            return HttpResponseRedirect(f"/download file/filename={converted_file['filename']}")
        return render(request, "converter/converter.html", {
            "form": submitted_form
        })

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    user_ip_address = get_client_ip(request)
    return render(request, "converter/index.html", {
        "number_of_visits": request.session['num_visits'],
        "session_key": request.session.session_key,
        "ip_address": user_ip_address
    })


class Login(View):
    def get(self, request):
        return render(request, "converter/login.html")

class Register(View):
    def get(self, request):
        return render(request, "converter/register.html")
class DownloadView(View):
    def get(self, request, filename):
        return render(request, "converter/filedownload.html", {
            "filename": filename
        })


class alpabet():
    excel_alphabet = []

    def generate_excel_alphabet():
        excel_alphabet = [ascii_uppercase[i]
                          for i in range(len(ascii_uppercase))]
        for i in range(26 + 1):
            if(i == 0):
                continue
        for j in range(26):
            excel_alphabet.append(excel_alphabet[i - 1] + excel_alphabet[j])
        return excel_alphabet


def download_file(request, filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__name__))
    filename = filename
    filepath = BASE_DIR + f"\\download\\{filename}"
    try:
        path = open(filepath, 'rb')
        mime_type, _ = mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        os.remove(filepath)
        return response
    except:
        return redirect("/quick-csv-converter")


class File_download_error(View):
    def get(self, request):
        return render(request, "converter/downloaderror.html")


def ConvertToXLSX(file: str):
    file_str = str(file)
    picked_filename_without_file_extension = file_str.replace(".csv", "")
    BASE_DIR = os.path.dirname(os.path.abspath(__name__))
    save_location = BASE_DIR + "\\download"
    filepath = BASE_DIR + f"\\temp\\{file_str}"
    save_file_name = f"{picked_filename_without_file_extension}_(converted).xlsx"
    save_file_path = f"{save_location}\\{save_file_name}"
    workbook = xlsx.Workbook(save_file_path)
    worksheet = workbook.add_worksheet()
    cell_format_currency = workbook.add_format()
    cell_format_number = workbook.add_format()
    cell_format_number.set_num_format('0')
    cell_format_currency.set_num_format('€#,##0.00')
    try:
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
                        worksheet.write(
                            f"{alphabet[i]}{idx + 1}", attributes[i])
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
                    worksheet.set_column(i, idx, column_length[i])
        workbook.close()
        with open(save_file_path, 'rb') as fh:
            return {"file": fh.read(),
                    "filename": save_file_name,
                    "filepath": save_file_path}
    except:
        return "NULL"
    finally:
        os.remove(filepath)
