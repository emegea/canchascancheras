<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import CrearCuentaForm  # Asegúrate de que esta importación esté presente
import datetime
from django.contrib import messages  # Para manejar mensajes de error
=======
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
>>>>>>> ddc112c0a6b8a95e2adb1335bec8eb678052fa63

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
    # En el form...
    # Si el method es un GET
    if request.method == 'GET':
        # Devuelvo el form vacio
        contexto['formulario_reservas'] = formularioReservas()
    # Si no, o sea que es un POST
    else:
        # Devuelvo el form con la data que cargó el cliente
        formulario = formularioReservas(request.POST)
        contexto['formulario_reservas'] = formulario
        # Valido el form
        if formulario.is_valid():
            print(request.POST)
            messages.success(request, "Tu reserva se envió correctamente")
            # Redirecciono
            return redirect('index')

    # Renderizo web/index.html que viene de /templates porque /url lo dice
    return render(request, "web/index.html", contexto)

#
# Vista de Quienes Somos
def somos(request):
    # Renderizo web/somos.html que viene de /templates porque /url lo dice
    return render(request, "web/somos.html")

#
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
    # Renderizo web/canchas.html que viene de /templates porque /url lo dice
    return render(request, "web/canchas.html", contexto)

#
# Vista de Reservas
def reservas(request):
    contexto = {
        'canchitas': [
<<<<<<< HEAD
            '/static/web/img/canchita-01.jpg'        
        ]
=======
            '/static/web/img/canchita-01.jpg'
        ]        
>>>>>>> ddc112c0a6b8a95e2adb1335bec8eb678052fa63
    }
    # En el form...
    # Si el method es un GET
    if request.method == 'GET':
        # Devuelvo el form vacio
        contexto['formulario_reservas'] = formularioReservas()
    # Si no, o sea que es un POST
    else:
        # Devuelvo el form con la data que cargó el cliente
        formulario = formularioReservas(request.POST)
        contexto['formulario_reservas'] = formulario
        # Valido el form
        if formulario.is_valid():
            print(request.POST)
            messages.success(request, "Tu reserva se envió correctamente")
            # Redirecciono
            return redirect('reservas')

    # Renderizo web/reservas.html que viene de /templates porque /url lo dice
    return render(request, "web/reservas.html", contexto)

#
# Vista de Contacto
def contacto(request):
<<<<<<< HEAD
    return render(request, "web/contacto.html")

=======
    contexto = {}
    # En el form...
    # Si el method es un GET
    if request.method == 'GET':
        # Devuelvo el form vacio
        contexto['formulario_contacto'] = formularioContacto()
    # Si no, o sea que es un POST
    else:
        # Devuelvo el form con la data que cargó el cliente
        formulario = formularioContacto(request.POST)
        contexto['formulario_contacto'] = formulario
        # Valido el form
        if formulario.is_valid():
            print(request.POST)
            messages.success(request, "El mensaje se envió correctamente")
            # Redirecciono
            return redirect('contacto')
        
    # Renderizo web/contacto.html que viene de /templates porque /url lo dice
    return render(request, "web/contacto.html", contexto)
#
>>>>>>> ddc112c0a6b8a95e2adb1335bec8eb678052fa63
# Vista de Login
def login(request):
    contexto = {}
    # En el form...
    # Si el method es un GET
    if request.method == 'GET':
        # Devuelvo el form vacio
        contexto['formulario_login'] = formularioLogin()
    # Si no, o sea que es un POST
    else:
        # Devuelvo el form con la data que cargó el cliente
        formulario = formularioLogin(request.POST)
        contexto['formulario_login'] = formulario
        # Valido el form
        if formulario.is_valid():
            print(request.POST)
            messages.success(request, "Usuario autentificado correctamente")
            # Redirecciono
            return redirect('login')

<<<<<<< HEAD
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
    return render(request, 'web/crear_cuenta.html', {'form': form})

# Vista de Inicio de Sesión Exitoso
def logeado_exito(request):
    # Lógica para manejar el inicio de sesión exitoso
    return render(request, 'logeado_exito.html')
=======
    # Renderizo web/login.html que viene de /templates porque /url lo dice
    return render(request, "web/login.html", contexto)

#
# Vista de logout
def logout(request):
    contexto = {}
    messages.success(request, "El usuario cerró su sesión correctamente.")
    # Renderizo web/logout.html que viene de /templates porque /url lo dice
    return render(request, "web/logout.html")

#
# Vista de Saludar con parámetros
def saludar(request, nombre):
    # Renderizo un HTML hecho por HttpResponse con parámetros
    return HttpResponse(f"<h1>Hola {nombre}</h1>")
>>>>>>> ddc112c0a6b8a95e2adb1335bec8eb678052fa63
