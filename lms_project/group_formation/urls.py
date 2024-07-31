from django.urls import path
from . import views

app_name = "group_formation"

urlpatterns = [
    path("", views.index, name="index"),
]
