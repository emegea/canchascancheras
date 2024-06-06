from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, formularioReservas, formularioContacto, formularioLogin
from .models import Cancha, Cliente, Reserva
import datetime


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Tu cuenta ha sido creada exitosamente')
            return redirect('home')  # Reemplaza 'home' con la vista a la que quieres redirigir después del registro
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = RegistroForm()
    return render(request, 'web/registro.html', {'form': form})



def chacan(request):
    return render(request, 'web/chachan.html')

def reserv(request):
    return render(request, 'web/reserv.html')    

def listar_canchas(request):
    canchas = Cancha.objects.all()
    return render(request, 'listar_canchas.html', {'canchas': canchas})

def detalle_cancha(request, id):
    cancha = get_object_or_404(Cancha, id=id)
    return render(request, 'detalle_cancha.html', {'cancha': cancha})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def detalle_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'listar_reservas.html', {'reservas': reservas})

def detalle_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    return render(request, 'detalle_reserva.html', {'reserva': reserva})

def crear_cuenta(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            login(request, user)
            return redirect('index')  # Redirige a la página de inicio u otra página después de la creación exitosa de la cuenta
    else:
        form = RegistroForm()
    return render(request, 'web/crear_cuenta.html', {'form': form})

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
    if request.method == 'GET':
        contexto['formulario_reservas'] = formularioReservas()
    else:
        formulario = formularioReservas(request.POST)
        contexto['formulario_reservas'] = formulario
        if formulario.is_valid():
            messages.success(request, "Tu reserva se envió correctamente")
            return redirect('index')
    return render(request, "web/index.html", contexto)

def somos(request):
    return render(request, "web/somos.html")

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

def reservas(request):
    contexto = {
        'canchitas': [
            '/static/web/img/canchita-01.jpg'
        ]        
    }
    if request.method == 'GET':
        contexto['formulario_reservas'] = formularioReservas()
    else:
        formulario = formularioReservas(request.POST)
        contexto['formulario_reservas'] = formulario
        if formulario.is_valid():
            messages.success(request, "Tu reserva se envió correctamente")
            return redirect('reservas')
    return render(request, "web/reservas.html", contexto)

def contacto(request):
    contexto = {}
    if request.method == 'GET':
        contexto['formulario_contacto'] = formularioContacto()
    else:
        formulario = formularioContacto(request.POST)
        contexto['formulario_contacto'] = formulario
        if formulario.is_valid():
            messages.success(request, "El mensaje se envió correctamente")
            return redirect('contacto')
    return render(request, "web/contacto.html", contexto)

def login_view(request):
    contexto = {}
    if request.method == 'GET':
        contexto['formulario_login'] = formularioLogin()
    else:
        formulario = formularioLogin(request.POST)
        contexto['formulario_login'] = formulario
        if formulario.is_valid():
            messages.success(request, "Usuario autentificado correctamente")
            return redirect('login')
    return render(request, "web/login.html", contexto)

def logout_view(request):
    contexto = {}
    messages.success(request, "El usuario cerró su sesión correctamente.")
    return render(request, "web/logout.html")

def saludar(request, nombre):
    return HttpResponse(f"<h1>Hola {nombre}</h1>")
