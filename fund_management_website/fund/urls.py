from django.urls import path
from fund import views

app_name = "fund"

urlpatterns = [
    path("", views.index, name = "index"),
]
