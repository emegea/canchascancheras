from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('somos', views.somos, name="somos"),
    path('canchas', views.canchas, name="canchas"),
    path('contacto', views.contacto, name="contacto"),
    #Compras
    path('buscar', views.buscar, name='buscar'),
    path('comprar_cancha/<int:cancha_id>/', views.comprar_cancha, name='comprar_cancha'),
    path('ventaCustom', views.ventaCustom, name="ventaCustom"),
    path('gracias', views.gracias, name="gracias"),
    #Auth
    path('login', auth_views.LoginView.as_view(template_name='web/login.html', redirect_field_name="index"), name="login"),
    # path('login', views.vistaLogin, name="login"),
    path('logout', views.vistaLogout, name="logout"),
    path('claveReset', auth_views.PasswordResetView.as_view(template_name='web/claveReset.html') , name="claveReset"),
]
