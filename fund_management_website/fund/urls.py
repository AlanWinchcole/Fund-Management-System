from django.urls import path
from fund import views

app_name = "fund"

urlpatterns = [
    path("", views.login, name = "index"),
    path("register/", views.register, name="register"),
]
