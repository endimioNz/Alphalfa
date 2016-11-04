#from alpha1.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=20,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Usuario'}))
	password = forms.CharField(label="Password", max_length=20,
		widget = forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Contraseña'}))


class VeterinarioForm(forms.ModelForm):
	class Meta:
		model = Veterinario
		fields = [
			"nombre", 
			"apellido",
			"dni", 
			"matricula",
			"domicilio_fiscal",
			"cp_domicilio_fiscal",
			"cuit",
			"codigo_area",
			"telefono1",
			"fecha_ingreso",
		]

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = [
		"descripcion",
		]

class ExplotacionForm(forms.ModelForm):
	class Meta:
		model = Explotacion
		fields = [
		"descripcion",
		]

class EspecieForm(forms.ModelForm):
	class Meta:
		model = Especie
		fields = [
		"descripcion",
		]

class MuestraForm(forms.ModelForm):
	class Meta:
		model = Muestra
		fields = [
		"descripcion",
		]

class ParametroForm(forms.ModelForm):
	class Meta:
		model = Parametros
		fields = [
		"descripcion",
		"tipo_de_dato",
		]

class EstablecimientoForm(forms.ModelForm):
	#categoria = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),required=True)
	categorias2 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Categoria.objects.all())
	explotacion2 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Explotacion.objects.all())
	
	class Meta:
		model = Establecimiento
		fields = [
		"nombre",
		"partido",
		"propietario",
		"RENSPA",
		"veterinario",
		"categorias2",
		"explotacion2",

		]
