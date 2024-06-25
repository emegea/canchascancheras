from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('somos', views.somos, name="somos"),
    path('canchas', views.canchas, name="canchas"),
    path('ventaCustom', views.ventaCustom, name="ventaCustom"),
    path('contacto', views.contacto, name="contacto"),
    path('gracias', views.gracias, name="gracias"),
    path('admin', views.admin, name="admin"),
    path('comprar_cancha/<int:cancha_id>/', views.comprar_cancha, name='comprar_cancha'),
    path('filtrar_canchas/', views.filtrar_canchas, name='filtrar_canchas'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
