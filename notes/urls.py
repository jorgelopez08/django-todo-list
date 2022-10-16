from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("delete/<int:note_id>", delete, name="delete_note"),
]
