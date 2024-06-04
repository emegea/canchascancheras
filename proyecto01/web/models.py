from django.db import models

# Definimos entidades
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    dni = models.IntegerField(verbose_name="DNI", unique=True)
    telefono = models.IntegerField(verbose_name="Teléfono")
    email = models.EmailField(max_length=100, verbose_name="Email")

# Creamos migraciones
# python manage.py makemigrations web