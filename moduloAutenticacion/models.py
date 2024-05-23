from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('asesor', 'Asesor'),
        ('cliente', 'Cliente'),
    )

    rol = models.CharField(max_length=15, choices=ROLE_CHOICES)
    #asdfsad
    pepe = 2


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    documento = models.CharField(max_length=10, unique=True) 
    usuario = models.OneToOneField('User', on_delete=models.CASCADE, related_name='cliente')
    class Meta:
        db_table = 'cliente'

class Asesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.OneToOneField('User', on_delete=models.CASCADE, related_name='asesor')




