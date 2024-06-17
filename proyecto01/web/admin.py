from django.contrib import admin
from .models import Cancha, Cliente, Venta, MensajeContacto

class CanchaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'longitud', 'ancho', 'tipo_suelo', 'tipo_red', 'iluminacion', 'marcador', 'gradas']
    search_fields = ['nombre', 'tipo_suelo', 'tipo_red']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['dni', 'apellido', 'nombre', 'email']
    search_fields = ['dni', 'apellido', 'nombre', 'email']

class VentaAdmin(admin.ModelAdmin):
    list_display = ['get_cancha_nombre', 'get_cliente_nombre', 'comentarios', 'get_longitud', 'get_ancho', 'get_tipo_suelo', 'get_tipo_red', 'get_iluminacion', 'get_marcador', 'get_gradas']
    search_fields = ['cancha__nombre', 'cliente__apellido', 'cliente__nombre']

    def get_cancha_nombre(self, obj):
        return obj.cancha.nombre if obj.cancha else None
    get_cancha_nombre.short_description = 'Cancha'

    def get_cliente_nombre(self, obj):
        return f"{obj.cliente.nombre} {obj.cliente.apellido}" if obj.cliente else None
    get_cliente_nombre.short_description = 'Cliente'

    def get_longitud(self, obj):
        return obj.cancha.longitud if obj.cancha else None
    get_longitud.short_description = 'Longitud'

    def get_ancho(self, obj):
        return obj.cancha.ancho if obj.cancha else None
    get_ancho.short_description = 'Ancho'

    def get_tipo_suelo(self, obj):
        return obj.cancha.tipo_suelo if obj.cancha else None
    get_tipo_suelo.short_description = 'Tipo de Suelo'

    def get_tipo_red(self, obj):
        return obj.cancha.tipo_red if obj.cancha else None
    get_tipo_red.short_description = 'Tipo de Red'

    def get_iluminacion(self, obj):
        return 'Sí' if obj.cancha and obj.cancha.iluminacion else 'No'
    get_iluminacion.short_description = 'Iluminación'

    def get_marcador(self, obj):
        return 'Sí' if obj.cancha and obj.cancha.marcador else 'No'
    get_marcador.short_description = 'Marcador Electrónico'

    def get_gradas(self, obj):
        return 'Sí' if obj.cancha and obj.cancha.gradas else 'No'
    get_gradas.short_description = 'Graderías'

class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'dni', 'telefono', 'email', 'mensaje', 'fecha_envio']
    search_fields = ['nombre', 'dni', 'email']

admin.site.register(Cancha, CanchaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(MensajeContacto, MensajeContactoAdmin)
