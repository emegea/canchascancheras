from django.urls import path
from .views import registro
from . import views

urlpatterns = [
    path('canchas/', views.listar_canchas, name='listar_canchas'),
    path('canchas/<int:id>/', views.detalle_cancha, name='detalle_cancha'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/<int:id>/', views.detalle_cliente, name='detalle_cliente'),
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('reservas/<int:id>/', views.detalle_reserva, name='detalle_reserva'),
    path('', views.index, name='index'),
    path('chacan/', views.chacan, name='chacan'),
    path('reserv/', views.reserv, name='reserv'),
    path('somos/', views.somos, name='somos'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login_view, name='login'),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('logout/', views.logout_view, name='logout'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    path('registro/', registro, name='registro'),
]
