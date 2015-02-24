from django import forms
from appgimnasio.models import HistorialIngresoCliente,Cliente
from django.contrib.auth.models import User

class IngresoUsuario(forms.Form):
	identificacion = forms.CharField()

class LoginUsuario(forms.Form):
	usuario = forms.CharField()
	contrasena = forms.CharField(widget=forms.PasswordInput())