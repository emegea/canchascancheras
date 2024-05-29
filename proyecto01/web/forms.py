from django import forms
from django.core.exceptions import ValidationError

# Formulario de la sección Contacto
class formularioContacto(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre'}
        )
    )
    dni = forms.IntegerField(
        label="DNI",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'DNI'}
        )
    )
    telefono = forms.IntegerField(
        label="Teléfono",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Teléfono'}
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Email'}
        )
    )
    mensaje = forms.CharField(
        label="Mensaje",
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Dejanos tu mensaje...'}
        )
    )    
    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError('El campo "nombre" solo puede contener letras')
        return self.cleaned_data["nombre"]

    def clean(self):
        return self.cleaned_data
        


#
#
# Formulario de la sección Resevas
class formularioReservas(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre'}
        )
    )

    CANCHAS_CHOICES = [
        ('cancha_de_5', 'Cancha de 5'),
        ('cancha_de_7', 'Cancha de 7'),
        ('cancha_de_11', 'Cancha de 11'),
    ]
    cancha = forms.ChoiceField(
        label="Elegí tu cancha",
        required=True,
        choices=CANCHAS_CHOICES,
        widget=forms.Select()
    )
    
    dni = forms.IntegerField(
        label="DNI",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'DNI'}
        )
    )
    HORARIOS_CHOICES = [
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
        ('21:00', '21:00'),
        ('22:00', '22:00'),
        ('23:00', '23:00'),
    ]
    horario = forms.ChoiceField(
        label="Elegí tu horario",
        required=True,
        choices=HORARIOS_CHOICES,
        widget=forms.Select()
    )
    
    telefono = forms.IntegerField(
        label="Teléfono",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Teléfono'}
        )
    )

    PAGO_CHOICES = [
        ('mercadopago', 'MercadoPago'),
        ('pago_mis_cuentas', 'Pago Mis Cuentas'),
        ('transferencia', 'Transferencia'),
    ]    
    metodo_pago = forms.ChoiceField(
        label="Elegí el método de pago",
        required=True,
        choices=PAGO_CHOICES,
        widget=forms.Select()
    )

# Formulario de Login
class formularioLogin(forms.Form):
    nombre_usuario = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre de usuario'}
        )
    )
    clave_usuario = forms.CharField(
        label="Clave Usuario",
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ingresá tu clave'}
        )
    )
