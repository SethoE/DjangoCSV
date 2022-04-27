from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quick-csv-converter", views.UploadFileView.as_view(), name="converter"),
    path("download file/filename=<str:filename>", views.DownloadView.as_view(), name="download"),
    path("download/filename=<str:filename>", views.download_file),
    path("file error", views.File_download_error.as_view())
]

