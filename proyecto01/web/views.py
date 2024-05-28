from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import CrearCuentaForm  # Asegúrate de que esta importación esté presente
import datetime
from django.contrib import messages  # Para manejar mensajes de error

# Vista del Index
def index(request):
    contexto = {
        'nombre': 'Carlos',
        'fecha_hora': datetime.datetime.now(),
        'canchas': [
            '/static/web/img/canchita-01.jpg',
            '/static/web/img/canchita-02.jpg',
            '/static/web/img/canchita-03.jpg',
            '/static/web/img/canchita-04.jpg',
        ]
    }
    return render(request, "web/index.html", contexto)

# Vista de Quienes Somos
def somos(request):
    return render(request, "web/somos.html")

# Vista de Canchas
def canchas(request):
    contexto = {
        'canchitas': [
            '/static/web/img/canchita-01.jpg',
            '/static/web/img/canchita-02.jpg',
            '/static/web/img/canchita-03.jpg',
            '/static/web/img/canchita-04.jpg',
            '/static/web/img/canchita-04.jpg',
            '/static/web/img/canchita-01.jpg',
            '/static/web/img/canchita-02.jpg',
            '/static/web/img/canchita-03.jpg',
        ]
    }
    return render(request, "web/canchas.html", contexto)

# Vista de Reservas
def reservas(request):
    contexto = {
        'canchitas': [
            '/static/web/img/canchita-01.jpg'        
        ]
    }
    return render(request, "web/reservas.html", contexto)

# Vista de Contacto
def contacto(request):
    return render(request, "web/contacto.html")

# Vista de Login
def login(request):
    return render(request, "web/login.html")

# Vista de Lista de Canchas
def lista_canchas(request):
    contexto = {
        'canchas': [
            'Cancha de 11',
            'Cancha de 7',
            'Cancha de 5'            
        ]
    }
    return render(request, 'web/lista_canchas.html', contexto)

# Nueva vista de Crear Cuenta
def crear_cuenta(request):
    if request.method == 'POST':
        form = CrearCuentaForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Encripta la contraseña
            user.save()
            login(request, user)  # Autentica y loguea al usuario
            return redirect('logeado_exito')  # Redirige a la página de inicio
    else:
        form = CrearCuentaForm()
    return render(request, 'web/formulario_crear_cuenta.html', {'form': form})

# Vista de Inicio de Sesión Exitoso
def logeado_exito(request):
    # Lógica para manejar el inicio de sesión exitoso
    return render(request, 'logeado_exito.html')