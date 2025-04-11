from django.urls import path
from .views import *

urlpatterns = [
    path("subjects/", subjects, name="subjects"),
    path("students/", students, name="students"),
    path("classes/", classes, name="classes"),
]
