from user.models import CustomUser
from django.db import models


class Clas(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Class")

    def __str__(self) -> str:
        return self.name

class Subject(models.Model):
    subject = models.CharField(max_length=255, null=False, blank=False, verbose_name="Subject's Name")
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.subject}"

class Grade(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="Grades")
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="Grades")
    grade = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.student} - {self.Subject} - {self.grade}"