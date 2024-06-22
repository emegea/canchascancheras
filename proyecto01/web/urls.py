from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('somos', views.somos, name="somos"),
    path('canchas', views.canchas, name="canchas"),
    path('ventaCustom', views.ventaCustom, name="ventaCustom"),
    path('contacto', views.contacto, name="contacto"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('gracias', views.gracias, name="gracias"),
    path('admin', views.admin, name="admin"),
    path('comprar_cancha/<int:cancha_id>/', views.comprar_cancha, name='comprar_cancha')
]
