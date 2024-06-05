from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from .models import Cancha, Cliente, Reserva

def listar_canchas(request):
    canchas = Cancha.objects.all()
    return render(request, 'listar_canchas.html', {'canchas': canchas})

def detalle_cancha(request, id):
    cancha = Cancha.objects.get(id=id)
    return render(request, 'detalle_cancha.html', {'cancha': cancha})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def detalle_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'listar_reservas.html', {'reservas': reservas})

def detalle_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    return render(request, 'detalle_reserva.html', {'reserva': reserva})

#vista de crear cuenta
def crear_cuenta(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            login(request, user)
            return redirect('logout')
    else:
        form = RegistroForm()
    return render(request, 'web/crear_cuenta', {'form': form})


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
            '/static/web/img/canchita-01.jpg'
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
            return redirect('reservas')

    # Renderizo web/reservas.html que viene de /templates porque /url lo dice
    return render(request, "web/reservas.html", contexto)

#
# Vista de Contacto
def contacto(request):
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

