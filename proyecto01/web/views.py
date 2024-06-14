from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *

#
# Vista del Index
def index(request):
    # Le paso los elementos de la db guardados como Canchas
    canchas = Cancha.objects.all()
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
    # En el form... Si el method es un GET
    if request.method == 'GET':
        # Devuelvo el form vacio
        contexto['formulario_venta'] = formularioAvanzado()
    # Si no, o sea que es un POST
    else:
        # Devuelvo el form con la data que cargó el cliente
        formulario = formularioAvanzado(request.POST)
        contexto['formulario_venta'] = formulario
        # Valido el form
        if formulario.is_valid():
            print(request.POST)
            messages.success(request, "Tu reserva se envió correctamente")
            # Redirecciono
            return redirect('index')

    return render(request, 'web/index.html', {'contexto': canchas})

#
# Vista de Quienes Somos
def somos(request):
    return render(request, "web/somos.html")
# Vista de Canchas
def canchas(request):
    canchas = Cancha.objects.all()
    return render(request, 'web/canchas.html', {'canchas': canchas})

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
            venta.cancha = cancha
            venta.save()
            messages.success(request, "Compra realizada con éxito!")
            return redirect('gracias')
    else:
        cliente_form = ClienteForm()
        venta_form = VentaForm()
    
    return render(request, 'web/comprar_cancha.html', {
        'cancha': cancha,
        'cliente_form': cliente_form,
        'venta_form': venta_form
    })


# Vista de Venta Personalizada
def ventaCustom(request):
    if request.method == 'POST':
        cancha_form = CanchaForm(request.POST)
        venta_form = VentaForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        
        if cancha_form.is_valid() and venta_form.is_valid() and cliente_form.is_valid():
            cliente = cliente_form.save()
            cancha = cancha_form.save()
            venta = venta_form.save(commit=False)
            venta.cliente = cliente
            venta.cancha = cancha
            venta.save()
            messages.success(request, "Venta concretada!")
            return redirect('/web/gracias')
    else:
        cancha_form = CanchaForm()
        venta_form = VentaForm()
        cliente_form = ClienteForm()

    return render(request, 'web/ventaCustom.html', {
        'cancha_form': cancha_form,
        'venta_form': venta_form,
        'cliente_form': cliente_form,
    })

# Vista de Venta
# def venta(request):
    # contexto = {}
    # if request.method == 'GET':
        # contexto['formulario_venta'] = formularioAvanzado()
    # else:
        # formulario = formularioAvanzado(request.POST)
        # contexto['formulario_venta'] = formulario
        # if formulario.is_valid():
            # formulario.save()
            # messages.success(request, "Venta concretada !")
            # return redirect('/web/gracias')

    # return render(request, 'web/venta.html', contexto)
 
# Vista de Gracias
def gracias(request):
    return render(request, "web/gracias.html")

# Vista de Contacto
def contacto(request):
    contexto = {}
    if request.method == 'GET':
        contexto['formulario_contacto'] = formularioContacto()
    else:
        formulario = formularioContacto(request.POST)
        contexto['formulario_contacto'] = formulario
        if formulario.is_valid():
            print(request.POST)
            messages.success(request, "El mensaje se envió correctamente")
            return redirect('contacto')
    return render(request, "web/contacto.html", contexto)

# Vista de Login
def login(request):
    contexto = {}
    # En el form... Si el method es un GET
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
    return render(request, "web/login.html", contexto)


# Vista de logout
def logout(request):
    contexto = {}
    messages.success(request, "El usuario cerró su sesión correctamente.")
    return render(request, "web/logout.html", contexto)

# Vista de Saludar con parámetros
def saludar(request, nombre):
    # Renderizo un HTML hecho por HttpResponse con parámetros
    return HttpResponse(f"<h1>Hola {nombre}</h1>")

# Vista de Admin
def admin(request):
    return redirect('/admin')

