from django.shortcuts import render
from user.models import CustomUser
from .models import *

def subjects(request):
    subjects = Subject.objects.all()
    context = { "subjects" : subjects }

    return render(request, "subjects.html", context)

def students(request):
    students = CustomUser.objects.all()
    context = { "students" : students }

    return render(request, "students.html", context)

def classes(request):
    classes = Clas.objects.all()
    context = { "classes" : classes }

    return render(request, "classes.html", context)

def grades_of_student(request, id):
    student = CustomUser.objects.filter(id=id).first()
    grades = Grade.objects.filter(student=student)
    context = {
        "student" : student,
        "grades" : grades
    }

    return render(request, "user/grades_of_a_student.html", context)
