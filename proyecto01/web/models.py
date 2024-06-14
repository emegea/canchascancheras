from django.db import models

class Cancha(models.Model):
    TIPOS_SUELO = [
        ('', 'Seleccione el tipo de suelo'),
        ('cesped_natural', 'Césped Natural'),
        ('cesped_artificial', 'Césped Artificial'),
        ('arcilla', 'Arcilla'),
        ('cemento', 'Cemento'),
        ('parquet', 'Parquet'),
    ]

    TIPOS_RED = [
        ('', 'Seleccione el tipo de red'),
        ('standard', 'Estándar'),
        ('reinforced', 'Reforzada'),
    ]

    nombre = models.CharField(max_length=100)
    longitud = models.DecimalField(max_digits=5, decimal_places=2)
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_suelo = models.CharField(max_length=50, choices=TIPOS_SUELO)
    tipo_red = models.CharField(max_length=50, choices=TIPOS_RED)
    iluminacion = models.BooleanField(default=False)
    marcador = models.BooleanField(default=False)
    gradas = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Venta(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.cancha} - {self.cliente}'
