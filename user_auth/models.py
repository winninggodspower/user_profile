from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name = "email address", max_length=254, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pic')

    def __str__(self):
        return self.username