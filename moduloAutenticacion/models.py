from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    ROLE_CHOICES = (
        ('asesor', 'Asesor'),
        ('cliente', 'Cliente'),
    )

    rol = models.CharField(max_length=15, choices=ROLE_CHOICES)
    #asdfsad
    idPersona = models.IntegerField(null = False)





