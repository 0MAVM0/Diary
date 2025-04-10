from django.contrib import admin
from .models import *

@admin.register(Clas)
class ClasAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = ["id", "name"]
    search_fields = ["name"]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["id", "subject", "clas"]
    list_filter = ["id", "subject"]
    search_fields = ["subject", "clas"]

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["id", "subject", "student", "grade", "created_at"]
    list_filter = ["id", "subject", "student"]
    search_fields = ["student"]
