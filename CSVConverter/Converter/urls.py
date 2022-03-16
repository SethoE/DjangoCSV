from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("csv-to-xlsx", views.UploadFileView.as_view(), name="converter"),
]
