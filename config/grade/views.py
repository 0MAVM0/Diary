from django.shortcuts import render, redirect
from user.models import CustomUser
from .models import *
from .forms import *

def grades_of_student(request, id):
    student = CustomUser.objects.filter(id=id).first()
    grades = Grade.objects.filter(student=student)
    context = {
        "student" : student,
        "grades" : grades
    }

    return render(request, "grades_of_a_student.html", context)

def grades_in_subject(request, id):
    subject = Subject.objects.filter(id=id).first()
    grades = Grade.objects.filter(subject=subject)
    context = {
        "subject" : subject,
        "grades" : grades
    }

    return render(request, "grades_in_a_subject.html", context)

def add_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("add_subject")
    else:
        form = ClassForm()
    context = { "form" : form }

    return render(request, "add_class.html", context)

def add_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("home") # HAS TO BE CHANGED
    else:
        form = SubjectForm()
    context = { "form" : form }

    return render(request, "add_subject.html", context)
