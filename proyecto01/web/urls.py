from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('somos', views.somos, name='somos'),
    path('canchas', views.canchas, name='canchas'),
    path('reservas', views.reservas, name='reservas'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.login, name='login'),
    path('crear_cuenta', views.crear_cuenta, name='crear_cuenta'),
    path('logeado_exito', views.logeado_exito, name='logeado_exito'),
    

#    path('saludar/<str:nombre>', views.saludar, name='saludar')
]
