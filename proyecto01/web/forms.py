from django import forms
<<<<<<< HEAD
from django.contrib.auth.models import User

class CrearCuentaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
=======
from django.core.exceptions import ValidationError

# Formulario de la sección Contacto
class formularioContacto(forms.Form):
    nombre = forms.CharField( label="Nombre", required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre'}
        ))
    dni = forms.IntegerField( label="DNI", required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'DNI'}
        ),
        error_messages={'invalid': 'El campo "DNI" solo puede contener números'}
    )
    telefono = forms.IntegerField( label="Teléfono", required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Teléfono'}
        ),
        error_messages={'invalid': 'El campo "Teléfono" solo puede contener números'}
    )
    email = forms.EmailField( label="Email", required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Email'}
        ),
        error_messages={'invalid': 'Ingresá una dirección de email válida. Ejemplo: nombre@email.com'}
    )
    mensaje = forms.CharField( label="Mensaje", required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Dejanos tu mensaje...'}
        ))

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not nombre.isalpha():
            raise ValidationError('El campo "nombre" solo puede contener letras')
        return nombre

    def clean_dni(self):
        dni = str(self.cleaned_data.get("dni"))
        if not dni.isdigit():
            raise ValidationError('El campo "DNI" solo puede contener números')
        if not len(dni) != 8:
            raise ValidationError('El campo "DNI" debe contener 8 dígitos')
        return dni
    
    def clean_telefono(self):
        telefono = str(self.cleaned_data.get("telefono"))
        if not telefono.isdigit():
            raise ValidationError('El campo "Teléfono" solo puede contener números')
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@" not in email:
            raise ValidationError('Ingesá una dirección de email válida. Ejemplo nombre@email.com')
        return email

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get("mensaje")
        if len(mensaje) < 10:    
            raise ValidationError('El campo "Mensaje" debe contener al menos 10 caracteres')
        return mensaje

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        dni = cleaned_data.get("dni")
        telefono = cleaned_data.get("telefono")
        email = cleaned_data.get("email")
        mensaje = cleaned_data.get("mensaje")
    
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
>>>>>>> ddc112c0a6b8a95e2adb1335bec8eb678052fa63
