from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Componente, Sede, Colaborador, Perfil_Usuario

# class ComponenteFormulario(forms.Form):
#     nombre = forms.CharField()
#     cantidad = forms.IntegerField()

class ComponenteFormulario(forms.ModelForm):
    class Meta:
        model = Componente
        #fields = ["nombre","cantidad","descripcion"]
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control", "placeholder":"Ingrese el nombre del componente"
            }),
            "cantidad": forms.NumberInput(attrs={
                "placeholder": "Ingrese la cantidad en stock"
            }),
            "precio": forms.NumberInput(attrs={
                "placeholder": "Ingrese el precio"
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Ingrese el detalle del producto"
            }),
        }
#El Siguiente codigo aplica la clase form a todos los campos automaticamente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica la clase "form-control" a todos los campos automáticamente
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get("class"):
                field.widget.attrs["class"] = "form-control"

class SedeFormulario(forms.ModelForm):
    class Meta:
        model = Sede
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control", "placeholder":"Ingrese el nombre de la Sede"
            }),
            "direccion": forms.TextInput(attrs={
                "placeholder": "Provincia, país | Ejemplo: San Jose, Costa Rica"
            }),
            "nro_tel": forms.TextInput(attrs={
                "placeholder": "xxxx-xx-xx"
            }),
        }
#El Siguiente codigo aplica la clase form a todos los campos automaticamente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica la clase "form-control" a todos los campos automáticamente
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get("class"):
                field.widget.attrs["class"] = "form-control"

class ColaboradorFormulario(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Ingrese el nombre del colaborador"
            }),
            "apellido": forms.TextInput(attrs={
                "placeholder": "Ingrese el apellido del colaborador"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Ingresar email: nombre.apellido@pcstore.com"
            }),
            "profesion": forms.TextInput(attrs={
                "placeholder":"Ingrese la profesión del colaborador"
            }),
        }
        # El Siguiente codigo aplica la clase form a todos los campos automaticamente

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica la clase "form-control" a todos los campos automáticamente
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get("class"):
                field.widget.attrs["class"] = "form-control"

class EditarUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","email")

class UsuarioPerfilForumlario(forms.ModelForm):
    class Meta:
        model = Perfil_Usuario
        fields = ["photo"]