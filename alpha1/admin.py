from django.contrib import admin

# Register your models here.

from alpha1.models import Veterinario, Especializacion, Categoria, Explotacion, TipoAnimal, TipoMuestra, Tecnicas, tecXmuestraXanim, Parametros, Motivos, Individuos, Establecimiento, Raza, InicioDeCarga, Protocolo
admin.site.register(Especializacion)
admin.site.register(Categoria)
admin.site.register(Explotacion)
admin.site.register(TipoAnimal)
admin.site.register(TipoMuestra)
admin.site.register(Tecnicas)
admin.site.register(Parametros)
admin.site.register(Motivos)
admin.site.register(Establecimiento)
admin.site.register(InicioDeCarga)
admin.site.register(Raza)
admin.site.register(Protocolo)
admin.site.register(tecXmuestraXanim)


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