from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

@login_required(login_url="login/")
def principal(request):
	return render(request, "principal.html")
	
def prueba(request):
	return render(request, "prueba.html")

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/login/?next=/")


def l_vet(request):
	queryset = Veterinario.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado Veterinario"
	}
	return render(request, "lista_vet.html", context)

def detalle(request, id=None):
	instance = get_object_or_404(Veterinario, id=id) 
	context = {
		"title": instance.id,
		"instance": instance,
	}
	return render(request, "detalle.html", context)

def l_categoria(request):
	queryset = Categoria.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Categorias"
	}
	return render(request, "lista_chik.html", context)

def l_explotacion(request):
	queryset = Explotacion.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado Explotaciones"
	}
	return render(request, "lista_chik.html", context)

def l_animal(request):
	queryset = TipoAnimal.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Animales"
	}
	return render(request, "lista_chik.html", context)

def l_muestra(request):
	queryset = TipoMuestra.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado Tipos de Muestra"
	}
	return render(request, "lista_chik.html", context)

def l_parametros(request):
	queryset = Parametros.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Parametros"
	}
	return render(request, "lista_parametros.html", context)

def l_establecimiento(request):
	queryset = Establecimiento.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Establecimientos"
	}
	return render(request, "lista_establecimiento.html", context)


def a_vet(request):
	form = VeterinarioForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#messages.success(request, "Creado Correctamente") solo funcionan en la misma pagina
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}
	return render(request, "form_base.html", context)

def a_categoria(request):
	form = CategoriaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect("/")

	context = {
		"form": form,
	}
	return render(request, "form_base.html", context)

def a_explotacion(request):
	form = ExplotacionForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect("/")
	context = {
		"form": form,
	}
	return render(request, "form_base.html", context)

def a_animal(request):
	form = TipoAnimalForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect("/")
	context = {
		"form": form
	}
	return render(request, "form_base.html", context)

def a_muestra(request):
	form = TipoMuestraForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect("/")
	context = {
		"form": form
	}
	return render(request, "form_base.html", context)

def a_parametro(request):
	form = ParametroForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect("/")
	context = {
		"form": form
	}
	return render(request, "form_base.html", context)

def a_establecimiento(request):
	form = EstablecimientoForm(request.POST or None)
	if form.is_valid():
		instance = form
		for c in request.POST.getlist('categorias2'):
			instance.categorias2.add(c)
		for x in request.POST.getlist('explotacion2'):
			instance.explotacion2.add(x)
		instance = form.save(commit=False)
		instance.save()

		return HttpResponseRedirect("/")
	context = {
		"form": form
	}
	return render(request, "form_base.html", context)
