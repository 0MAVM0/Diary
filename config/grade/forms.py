from django import forms
from .models import *

class ClassForm(forms.ModelForm):
    class Meta:
        model = Clas
        fields = ("name",)

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ("subject", "clas")

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ("subject", "student", "grade")
