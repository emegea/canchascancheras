from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages

# Vista del Index
def index(request):
    contexto = {
        'nombre': 'Carlos',
        'fecha_hora': datetime.datetime.now(),
        'canchas': [
            '/static/web/img/canchita-01.jpg',
            '/static/web/img/canchita-02.jpg',
            '/static/web/img/canchita-03.jpg',
            '/static/web/img/canchita-04.jpg'
        ]
    }
    # Si el method es un GET
    if request.method == 'GET':
        # Devuelvo el form vacio
        contexto['formulario_reservas'] = formularioReservas()
    # Si no, o sea que es un POST
    else:
        # Devuelvo el form con la data que cargó el cliente
        contexto['formulario_reservas'] = formularioReservas(request.POST)
        # Valido el form
        # ...
        # Chequeando con un print
        print(request.POST)
        # Redirecciono
        # redirect('index')


 
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
            '/static/web/img/canchita-03.jpg'
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
    # Si el method es un GET
    if request.method == 'GET':
        # Devuelvo el form vacio
        contexto['formulario_reservas'] = formularioReservas()
    # Si no, o sea que es un POST
    else:
         # Devuelvo el form con la data que cargó el cliente
        contexto['formulario_reservas'] = formularioReservas(request.POST)
        # Valido el form
        # ...
        # Chequeando con un print
        print(request.POST)
        # Redirecciono
        # redirect('index')
    return render(request, "web/reservas.html", contexto)

# Vista de Contacto
def contacto(request):
    contexto = {}
    # Si el method es un GET
    if request.method == 'GET':
        # Devuelvo el form vacio
        contexto['formulario_contacto'] = formularioContacto()
    # Si no, o sea que es un POST
    else:
        # Devuelvo el form con la data que cargó el cliente
        formulario = formularioContacto(request.POST)
        contexto['formulario_login'] = formulario
        # Valido el form
        if formulario.is_valid():
            messages.success(request, "Formulario enviado correctamente")
            # Redirecciono
            redirect('login')
    return render(request, "web/contacto.html", contexto)

# Vista de Login
def login(request):
    contexto = {}
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
            # Redirecciono
            redirect('login')

    return render(request, "web/login.html", contexto)

# Vista de logout
def logout(request):
    return render(request, "web/logout.html")


def saludar(request, nombre):
    return HttpResponse(f"<h1>Hola {nombre}</h1>")
