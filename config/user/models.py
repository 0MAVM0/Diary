from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birth_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Birth Date")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Address")
    phone = models.IntegerField(null=True, blank=True, verbose_name="Phone Number")
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True, verbose_name="Avatar")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.username} - {self.phone} - {self.address}"
