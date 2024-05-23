from django.shortcuts import render
# from django.http import HttpResponse
import datetime

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
            '/static/web/img/canchita-01.jpg'        ]
    }
    return render(request, "web/reservas.html", contexto)

# Vista de Contacto
def contacto(request):
    return render(request, "web/contacto.html")

# Vista de Reservas
def login(request):
    return render(request, "web/login.html")

# Vista de Lista de Canchas
# (por si se necesita hacer un listado para luego cargarlo o algo así)
def lista_canchas(request):
    contexto = {
        'canchas': [
            'Cancha de 11',
            'Cancha de 7',
            'Cancha de 5'            
        ]
    }
    return render(request, 'web/lista_canchas.html', contexto)

# def saludar(request, nombre):
#     return HttpResponse(f"<h1>Hola {nombre}</h1>")
