from django.db import models
import datetime 


# 1. Relación de Uno a Muchos entre Cliente y Venta,
# Un cliente puede hacer muchas compras (Venta).

# 2. Relación de Muchos a Muchos entre Venta y Cancha
# Una venta puede incluir muchas canchas y
# una cancha puede estar en muchas ventas.

    
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
    canchas = models.ManyToManyField(Cancha, related_name='ventas')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True, null=True)
    is_custom = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if self.is_custom and not self.nombre:
            total_custom_sales = Venta.objects.filter(is_custom=True).count()
            self.nombre = f'Compra Custom - {total_custom_sales + 1}'
        else:
            total_custom_sales = Venta.objects.filter(is_custom=True).count()
            self.nombre = f'Compra - {total_custom_sales + 1}'
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} - {self.cliente}'    

# Modelo para manejar mensajes del formulario de contacto
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensaje de {self.nombre} - {self.email}'

#modelo sugerencia

class Sugerencia(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    sugerencia = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class MensajeAgradecimiento(models.Model):
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)      