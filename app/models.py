from django.db import models

# Create your models here.
from django.db import models

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=1000)
    ano = models.IntegerField()