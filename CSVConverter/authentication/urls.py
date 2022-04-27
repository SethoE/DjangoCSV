from django.urls import path
from . import views

urlpatterns = [
    path("login", views.Login.as_view(), name="sign-in"),
    path("register", views.Register.as_view(), name="sign-up"),
    path("logout", views.Logout.as_view(), name="sign-out"),
]

