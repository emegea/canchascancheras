from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('somos/', views.somos, name="somos"),
    path('canchas/', views.canchas, name="canchas"),
    path('contacto/', views.contacto, name="contacto"),
    path('sugerencias/enviar/', views.enviar_sugerencia, name='enviar_sugerencia'),
    path('sugerencias/gracias/', views.gracias, name='gracias'),
    #Compras
    path('buscar/', views.buscar, name='buscar'),
    path('comprar_cancha/<int:cancha_id>/', views.comprar_cancha, name='comprar_cancha'),
    path('cancha_personalizada/', views.cancha_personalizada, name="cancha_personalizada"),
    path('gracias/', views.gracias, name="gracias"),
    # Vistas basadas en clases
    path('crear_cancha', CrearCancha.as_view(), name="crear_cancha"),
    path('listar_canchas/', ListarCanchas.as_view(), name='listar_canchas'),
    path('actualizar_cancha/<int:id>/', ActualizarCancha.as_view(), name='actualizar_cancha'),
    path('eliminar_cancha/<int:id>/', EliminarCancha.as_view(), name='eliminar_cancha'),
    # Vistas Auth
    path('registro', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='web/login.html', redirect_field_name="index"), name="login"),
    # path('login', views.vistaLogin, name="login"),
    path('logout/', views.vistaLogout, name="logout"),
    path('cambiar_clave/', auth_views.PasswordResetView.as_view(template_name="cambiar_clave.html"), name='password_reset'),
    path('cambiar_clave_enviar/', auth_views.PasswordResetDoneView.as_view(template_name="cambiar_clave_enviar.html"), name='password_reset_done'),
    path('cambiar_clave/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="cambiar_clave_confirmar.html"), name='password_reset_confirm'),
    path('cambiar_clave_ok/', auth_views.PasswordResetCompleteView.as_view(template_name="cambiar_clave_ok.html"), name='password_reset_complete'),

]