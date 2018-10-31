from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile_pics/', null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
