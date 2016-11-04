from django.contrib import admin

# Register your models here.

from alpha1.models import Veterinario, EliminacionProtocolo, ValoresReferencia, DetalleAnalisis, CategoriaE, Especializacion, Categoria, Explotacion, Especie, Muestra, Diagnostico, Parametros, Motivos, Individuos, Establecimiento, Raza, SolicitudAnalisis, Protocolo
admin.site.register(Especializacion)
admin.site.register(Categoria)
admin.site.register(CategoriaE)
admin.site.register(Explotacion)
admin.site.register(Especie)
admin.site.register(Muestra)
admin.site.register(Diagnostico)
admin.site.register(Parametros)
admin.site.register(Motivos)
admin.site.register(Establecimiento)
admin.site.register(SolicitudAnalisis)
admin.site.register(Raza)
admin.site.register(Protocolo)
admin.site.register(EliminacionProtocolo)
admin.site.register(ValoresReferencia)
admin.site.register(DetalleAnalisis)



@admin.register(Individuos)
class IndividuosAdmin(admin.ModelAdmin):
	list_display = ('identificacion', 'nombre', 'sexo',)
	fieldsets = (
       (None, {
            'fields': ('identificacion',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('nombre', 'edad', 'sexo', 'obs'),
        }),
    )

@admin.register(Veterinario) 
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'matricula', 'telefono1',)
    fieldsets = (
       ('Datos Personales', {
            'fields': (('apellido', 'nombre'), ('dni', 'matricula')),  
        }),
        ('Datos de Contacto', {
            'classes': ('collapse',),
            'fields': (('domicilio_particular', 'cp_domicilio_particular'),
                ('codigo_area', 'telefono1', 'telefono2'),
                'email',)                
        }),
        ('Datos Fiscales', {
            'classes': ('collapse',),
            'fields': (('domicilio_fiscal', 'cp_domicilio_fiscal', 'cuit')),
        }),
        ('Otros Datos', {
            'classes': ('collapse',),
            'fields': (('fecha_ingreso', 'fecha_baja'), ('acreditacion_brucelosis', 'acreditacion_aie')),
        }),
    )