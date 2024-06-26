from .forms import *
from .models import *
from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test

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

#Vista de búsqueda parametrizada filtrando
@login_required
def buscar(request):
    canchas = []

    if request.method == "GET" and not request.GET:
        formulario = CanchaForm()
    else:
        formulario = CanchaForm(request.GET)
        if formulario.is_valid():
            tipo_suelo = formulario.cleaned_data.get('tipo_suelo')
            tipo_red = formulario.cleaned_data.get('tipo_red')
            iluminacion = formulario.cleaned_data.get('iluminacion')
            marcador = formulario.cleaned_data.get('marcador')
            gradas = formulario.cleaned_data.get('gradas')

            canchas = Cancha.objects.all()  
            if tipo_suelo:
                canchas = canchas.filter(tipo_suelo=tipo_suelo)
            if tipo_red:
                canchas = canchas.filter(tipo_red=tipo_red)
            if iluminacion is not None:
                canchas = canchas.filter(iluminacion=iluminacion)
            if marcador is not None:
                canchas = canchas.filter(marcador=marcador)
            if gradas is not None:
                canchas = canchas.filter(gradas=gradas)

    return render(request, 'buscar.html', {
        'formulario': formulario,
        'canchas': canchas
    })

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
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('/admin/')  # Redirige a la página admin después del login
    else:
        form = AuthenticationForm()
    
    return render(request, 'web/login.html', {'formulario_login': form})

# Vista de Logout
def vistaLogout(request):
    #Llamo al logout de django
    logout(request)
    messages.success(request, "El usuario cerró su sesión correctamente.")
    return redirect('index')

# Vista de Admin
def admin(request):
    return redirect('/admin')

# Vista de claveReset
def claveReset(request):
    messages.success(request, "La clave fue reseteada correctamente.")
    return render(request, "claveReset.html")
