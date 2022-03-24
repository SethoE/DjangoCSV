from django.urls import path
from django.views.static import serve
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("csv-to-xlsx", views.UploadFileView.as_view(), name="converter"),
    path("download file/<str:filename>", views.DownloadView.as_view(), name="download"),
    path("download", views.download_file),
    path("file error", views.File_download_error.as_view())
]

