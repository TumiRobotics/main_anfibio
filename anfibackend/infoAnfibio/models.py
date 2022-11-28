from django.db import models

# Create your models here.
class usuariosAnfibio(models.Model):
    nombre = models.CharField(max_length=64,default='')
    apellido = models.CharField(max_length=64,default='')
    usuario = models.CharField(max_length=64,default='')
    email = models.CharField(max_length=64,default='')
    nroCelular = models.CharField(max_length=64,default='')
    contra = models.CharField(max_length=64,default='')
    codigoUsr = models.CharField(max_length=64,default='OP-0000')
    urlFoto = models.CharField(max_length=512,default='')

class botesAnfibio(models.Model):
    codigoBote = models.CharField(max_length=512,default='')
    urlBote = models.CharField(max_length=512,default='')