from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True,default=0)
    gender = models.CharField(max_length=20,default=" ")
    year = models.IntegerField(null=True,blank=True,default=0)