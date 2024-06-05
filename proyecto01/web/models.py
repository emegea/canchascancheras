from django.db import models
from django.contrib.auth.models import User


# Definimos entidades

class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=50)
    tipo_superficie = models.CharField(max_length=50)
    precio_alquiler_hora = models.DecimalField(max_digits=8, decimal_places=2)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

class Reserva(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")


# Creamos migraciones
# python manage.py makemigrations (web):especifica la app,opcional,segun cantidad de apps
#ejecutamos migraciones
#python manage.py migrate web