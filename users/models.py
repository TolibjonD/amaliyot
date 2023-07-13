from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='users/', default='users/default.png')

    def get_full_name(self) -> str:
        return super().get_full_name()