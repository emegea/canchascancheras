from django.urls import path
from . import views

urlpatterns = [
    path('canchas', views.listar_canchas, name='listar_canchas'),
    path('canchas<int:id>/', views.detalle_cancha, name='detalle_cancha'),
    path('clientes', views.listar_clientes, name='listar_clientes'),
    path('clientes<int:id>/', views.detalle_cliente, name='detalle_cliente'),
    path('reservas', views.listar_reservas, name='listar_reservas'),
    path('reservas<int:id>/', views.detalle_reserva, name='detalle_reserva'),
    path('', views.index, name='index'),
    path('somos', views.somos, name='somos'),
    #path('canchas', views.canchas, name='canchas'),
    #path('reservas', views.reservas, name='reservas'),
    path('contacto', views.contacto, name='contacto'),
    path('login', views.login, name='login'),
    path('crear_cuenta', views.crear_cuenta, name='crear_cuenta'),
   
    #path('logeado_exito', views.logeado_exito, name='logeado_exito'),
    

#    path('saludar/<str:nombre>', views.saludar, name='saludar')
]
