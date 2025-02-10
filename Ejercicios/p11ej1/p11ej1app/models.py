from django.db import models

# Create your models here.
class Login(models.Model):
    nombre=models.CharField(unique=True,max_length=80)
    contra=models.CharField(unique=True,min_length=4)

