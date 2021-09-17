from django.db import models

# Create your models here.
class tipo_de_mascota(models.Model):
    pk_tipo_de_mascotae = models.AutoField(primary_key=True, null=False, blank=False)
    descripcion= models.CharField(max_length=50, null=False, blank=False)
    nombre= models.CharField(max_length=50, null=False, blank=False)

class raza(models.Model):
    pk_raza = models.AutoField(primary_key=True, null=False, blank=False)
    descripcion= models.CharField(max_length=50, null=False, blank=False)
    nombre= models.CharField(max_length=50, null=False, blank=False)

class Mascota(models.Model):
    pk_tipo_de_mascotae = models.AutoField(primary_key=True, null=False, blank=False)
    nombre= models.CharField(max_length=50, null=False, blank=False)
    edad=models.CharField(max_length=50, null=False, blank=False)
    registro= models.CharField(max_length=50, null=False, blank=False)