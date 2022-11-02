from django.contrib.auth.models import AbstractUser
from django.db import models


class UserData(AbstractUser):
    first_name = models.CharField(max_length=49)
    last_name = models.CharField(max_length=99)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    