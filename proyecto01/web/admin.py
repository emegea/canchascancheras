from django.contrib import admin
from .models import Cancha, Cliente, Venta, MensajeContacto

class CanchaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'longitud', 'ancho', 'tipo_suelo', 'tipo_red', 'iluminacion', 'marcador', 'gradas']
    search_fields = ['nombre', 'tipo_suelo', 'tipo_red']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['dni', 'apellido', 'nombre', 'email']
    search_fields = ['dni', 'apellido', 'nombre', 'email']

class VentaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'get_cliente_nombre', 'get_canchas', 'comentarios', 'fecha']
    search_fields = ['cancha', 'nombre', 'cliente__apellido', 'cliente__nombre']

    def get_cliente_nombre(self, obj):
        return f"{obj.cliente.nombre} {obj.cliente.apellido}" if obj.cliente else None
    get_cliente_nombre.short_description = 'Cliente'

    def get_canchas(self, obj):
        return ', '.join([cancha.nombre for cancha in obj.canchas.all()])
    get_canchas.short_description = 'Canchas'

class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'dni', 'telefono', 'email', 'mensaje', 'fecha_envio']
    search_fields = ['nombre', 'dni', 'email']

admin.site.register(Cancha, CanchaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(MensajeContacto, MensajeContactoAdmin)
