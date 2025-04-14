from django.urls import path
from .views import *

urlpatterns = [
    path("subjects/", subjects, name="subjects"),
    path("students/", students, name="students"),
    path("classes/", classes, name="classes"),
    path("student/<int:id>/", grades_of_student, name="grades_of_a_student"),
    path("subject/<int:id>/", grades_in_subject, name="grades_in_a_subject"),
]
