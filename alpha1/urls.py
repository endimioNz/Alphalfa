from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as vw
from alpha1 import views 
from .forms import LoginForm

urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^login/', vw.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/', views.logout_view),
    url(r'^(?P<id>\d+)/$', views.detalle, name="detalle"),
	url(r'^lista_vet/$', views.l_vet),
	url(r'^lista_categoria/$', views.l_categoria),
	url(r'^lista_explotaciones/$', views.l_explotacion),
	url(r'^lista_animales/$', views.l_animal),
	url(r'^lista_muestras/$', views.l_muestra),
	url(r'^lista_parametros/$', views.l_parametros),
	url(r'^lista_establecimiento/$', views.l_establecimiento),
	url(r'^vet_form/$', views.a_vet),
	url(r'^categoria_form/$', views.a_categoria),
	url(r'^explotacion_form/$', views.a_explotacion),
	url(r'^animal_form/$', views.a_animal),
	url(r'^muestra_form/$', views.a_muestra),
	url(r'^parametro_form/$', views.a_parametro),
	url(r'^establecimiento_form/$', views.a_establecimiento),

]
