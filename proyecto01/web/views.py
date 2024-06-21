from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import *
from .models import *

# Vista del Index
def index(request):
    # Obtengo las últimas 4 canchas publicadas
    canchas = Cancha.objects.all().order_by('-id')[:4]

    contexto = {
        'nombre': 'Carlos',
        'fecha_hora': datetime.datetime.now(),
        'canchas': canchas
    }
    return render(request, 'index.html', {'contexto': canchas})

# Vista de Quienes Somos
def somos(request):
    return render(request, "somos.html")

# Vista de Canchas
def canchas(request):
    canchas = Cancha.objects.all()
    return render(request, 'canchas.html', {'canchas': canchas})

# Vista para manejar la compra de una cancha estándar
def comprar_cancha(request, cancha_id):
    cancha = get_object_or_404(Cancha, id=cancha_id)
    
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        venta_form = VentaForm(request.POST)
        
        if cliente_form.is_valid() and venta_form.is_valid():
            cliente = cliente_form.save()
            venta = venta_form.save(commit=False)
            venta.cliente = cliente
            venta.save()
            venta.canchas.add(cancha)
            messages.success(request, "Compra realizada con éxito!")
            return redirect('gracias')
    else:
        cliente_form = ClienteForm()
        venta_form = VentaForm()
    
    return render(request, 'comprar_cancha.html', {
        'cancha': cancha,
        'cliente_form': cliente_form,
        'venta_form': venta_form
    })

# Vista de Venta Personalizada
def ventaCustom(request):
    if request.method == 'POST':
        cancha_form = CanchaForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        venta_form = VentaForm(request.POST)
        
        if cancha_form.is_valid() and venta_form.is_valid() and cliente_form.is_valid():
            cliente = cliente_form.save()
            # cancha = cancha_form.save()
            venta = venta_form.save(commit=False)
            venta.cliente = cliente
            venta.is_custom = True  # Marcar la venta como personalizada
            venta.save()
            venta.canchas.add()  # Agregar la cancha a la venta
            messages.success(request, "¡Venta concretada!")
        return redirect('/gracias')
    else:
        cancha_form = CanchaForm()
        venta_form = VentaForm()
        cliente_form = ClienteForm()

    return render(request, 'ventaCustom.html', {
        'cancha_form': cancha_form,
        'venta_form': venta_form,
        'cliente_form': cliente_form,
    })

# Vista de Gracias
def gracias(request):
    return render(request, "gracias.html")

# Vista de Contacto
def contacto(request):
    contexto = {}
    if request.method == 'GET':
        contexto['formulario_contacto'] = formularioContacto()
    else:
        formulario = formularioContacto(request.POST)
        contexto['formulario_contacto'] = formulario
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El mensaje se envió correctamente")
            return redirect('contacto')
    return render(request, "contacto.html", contexto)

# Vista de Login
def vistaLogin(request):
    if request.method == 'POST':
        formulario = formularioLogin(request.POST)
        if formulario.is_valid():
            # Acá iría la lógica para autenticar al usuario
            messages.success(request, f"Hola {Cliente.nombre}, Bienvenid@ !")
            return redirect('index')
    else:
        formulario = formularioLogin()
    return render(request, 'login.html', {'formulario_login': formulario})

# Vista de Logout
def vistaLogout(request):
    #Llamo al logout de django
    logout(request)
    messages.success(request, "El usuario cerró su sesión correctamente.")
    return redirect('index')

# Vista de claveReset
def claveReset(request):
    messages.success(request, "La clave fue reseteada correctamente.")
    return render(request, "claveReset.html")
