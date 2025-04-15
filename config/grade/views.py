from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from user.models import CustomUser
from .models import *
from .forms import *

def subjects(request):
    subjects = Subject.objects.all()
    pages = Paginator(subjects, 2)
    page_number = request.GET.get("page")
    page_obj = pages.get_page(page_number)
    context = { "page_obj" : page_obj }
 
    return render(request, "subjects.html", context)

def students(request):
    students = CustomUser.objects.all()
    pages = Paginator(students, 2)
    page_number = request.GET.get("page")
    page_obj = pages.get_page(page_number)
    context = { "page_obj" : page_obj }

    return render(request, "students.html", context)

def grades_of_student(request, id):
    student = CustomUser.objects.filter(id=id).first()
    grades = Grade.objects.filter(student=student)
    pages = Paginator(grades, 2)
    page_number = request.GET.get("page")
    page_obj = pages.get_page(page_number)
    context = {
        "student" : student,
        "page_obj" : page_obj
    }

    return render(request, "grades_of_a_student.html", context)

def grades_in_subject(request, id):
    subject = Subject.objects.filter(id=id).first()
    grades = Grade.objects.filter(subject=subject)
    pages = Paginator(grades, 2)
    page_number = request.GET.get("page")
    page_obj = pages.get_page(page_number)
    context = {
        "subject" : subject,
        "page_obj" : page_obj
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

            return redirect("evaluate")
    else:
        form = SubjectForm()
    context = { "form" : form }

    return render(request, "add_subject.html", context)

def evaluate(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = GradeForm()
    context = { "form" : form }

    return render(request, "evaluate.html", context)
