from django import forms
from .models import Cancha, Cliente, Venta

class formularioVenta(forms.ModelForm):
    fecha = forms.DateTimeField(
        label='Fecha de compra',  # Cambia el label del campo
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Venta
        fields = ['cancha', 'cliente', 'fecha']

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
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Ingresá tu clave'}
        )
    )
    
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
            raise forms.ValidationError('El campo "nombre" solo puede contener letras')
        return nombre

    def clean_dni(self):
        dni = str(self.cleaned_data.get("dni"))
        if not dni.isdigit():
            raise forms.ValidationError('El campo "DNI" solo puede contener números')
        if not len(dni) != 8:
            raise forms.ValidationError('El campo "DNI" debe contener 8 dígitos')
        return dni
    
    def clean_telefono(self):
        telefono = str(self.cleaned_data.get("telefono"))
        if not telefono.isdigit():
            raise forms.ValidationError('El campo "Teléfono" solo puede contener números')
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@" not in email:
            raise forms.ValidationError('Ingesá una dirección de email válida. Ejemplo nombre@email.com')
        return email

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get("mensaje")
        if len(mensaje) < 10:    
            raise forms.ValidationError('El campo "Mensaje" debe contener al menos 10 caracteres')
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
# Form avanzado hecho con GPT
class formularioAvanzado(forms.Form):
    longitud = forms.DecimalField(
        label='Largo (m)',
        widget=forms.NumberInput(attrs={'placeholder': 'Largo (m)'}),
        min_value=10,
        max_value=120,
        required=False
    )
    ancho = forms.DecimalField(
        label='Ancho (m)',
        widget=forms.NumberInput(attrs={'placeholder': 'Ancho (m)'}),
        min_value=10,
        max_value=90,
        required=False
    )
    opciones_suelo = [
        ('', 'Seleccione el tipo de suelo'),
        ('cesped_natural', 'Césped Natural'),
        ('cesped_artificial', 'Césped Artificial'),
        ('arcilla', 'Arcilla'),
        ('cemento', 'Cemento'),
        ('parquet', 'Parquet'),
    ]
    tipo_suelo = forms.ChoiceField(
        label='Tipo de Suelo',
        widget=forms.Select(attrs={'placeholder': 'Tipo de Suelo'}),
        choices=opciones_suelo,
        required=False
    )
    opciones_red = [
        ('', 'Seleccione el tipo de red'),
        ('standard', 'Estándar'),
        ('reinforced', 'Reforzada'),
    ]
    tipo_red = forms.ChoiceField(
        label='Tipo de Red',
        widget=forms.Select(attrs={'placeholder': 'Tipo de Red'}),
        choices=opciones_red,
        required=False
    )
    iluminacion = forms.BooleanField(
        label='Iluminación',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'placeholderCustom',
                'placeholder': 'Iluminación'
            }),
        required=False
    )
    marcador = forms.BooleanField(
        label='Marcador Electrónico',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'placeholderCustom',
                'placeholder': 'Marcador Electrónico'
            }),
        required=False
    )
    gradas = forms.BooleanField(
        label='Graderías',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'placeholderCustom',
                'placeholder': 'Graderías'
            }),
        required=False
    )
    campo_texto = forms.CharField(
        label='Comentarios Adicionales',
        widget=forms.Textarea(attrs={'placeholder': 'Comentarios Adicionales'}),
        max_length=255,
        required=False
    )

#  Form basado en model

class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = ['longitud', 'ancho', 'tipo_suelo', 'tipo_red', 'iluminacion', 'marcador', 'gradas']
        widgets = {
            'longitud': forms.NumberInput(attrs={'placeholder': 'Largo (m)'}),
            'ancho': forms.NumberInput(attrs={'placeholder': 'Ancho (m)'}),
            'tipo_suelo': forms.Select(attrs={'placeholder': 'Seleccione el tipo de suelo'}),
            'tipo_red': forms.Select(attrs={'placeholder': 'Seleccione el tipo de red'}),
            'iluminacion': forms.CheckboxInput(attrs={'class': 'placeholderCustom', 'placeholder': 'Iluminación'}),
            'marcador': forms.CheckboxInput(attrs={'class': 'placeholderCustom', 'placeholder': 'Marcador Electrónico'}),
            'gradas': forms.CheckboxInput(attrs={'class': 'placeholderCustom', 'placeholder': 'Graderías'}),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['comentarios']
        widgets = {
            'comentarios': forms.Textarea(attrs={'placeholder': 'Comentarios Adicionales'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'apellido', 'nombre', 'email']
        widgets = {
            'dni': forms.TextInput(attrs={'placeholder': 'DNI'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }