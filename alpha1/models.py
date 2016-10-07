from django.db import models
from django.core.urlresolvers import reverse 

# Create your models here.
class Especializacion(models.Model):
	descripcion = models.CharField("Especializacion", max_length=30)

	def __str__(self):
		return ('%s')%(self.descripcion)

class Veterinario(models.Model):
	nombre = models.CharField("Nombre", max_length=30)
	apellido = models.CharField("Apellido", max_length=30)
	matricula = models.CharField(max_length=10, unique=True)
	dni = models.CharField(max_length=8, unique=True)
	domicilio_particular = models.CharField("Domicilio Particular", max_length=30, blank=True, null=True)
	cp_domicilio_particular = models.CharField("Codigo Postal del Dom.Part.", max_length=4, blank=True, null=True)
	domicilio_fiscal = models.CharField("Domicilio Fiscal", max_length=30)
	cp_domicilio_fiscal = models.CharField("Codigo Postal del Dom.Fisc", max_length=4)
	email = models.EmailField("Email", blank=True, null=True)
	cuit = models.CharField("C.U.I.T.", max_length=13)
	codigo_area = models.CharField("Codigo de Area", max_length=4)
	telefono1 = models.CharField("Telefono 1", max_length=15)
	telefono2 = models.CharField("Telefono 2", max_length=15, blank=True, null=True)
	fecha_ingreso = models.DateField("Fecha de Ingreso", auto_now=False)
	fecha_baja = models.DateField("Fecha de Baja", auto_now=False, null=True, blank=True)
	acreditacion_brucelosis = models.CharField("Numero de Acreditacion de Brucelosis", max_length=15, null=True, blank=True)
	acreditacion_aie = models.CharField("Numero de Acreditacion de A.I.E.", max_length=15, null=True, blank=True)
	especializaciones = models.ManyToManyField(Especializacion)

	def __str__(self):
		return ('%s, %s')%(self.apellido, self.nombre)

	def get_absolute_url(self):
		return reverse("alpha:detalle", kwargs={"id": self.id}) #keyword args

class Categoria(models.Model):
	descripcion = models.CharField("Categoria", max_length=30)

	def __str__(self):
		return ('%s')%(self.descripcion)

class Explotacion(models.Model):
	descripcion = models.CharField("Explotacion", max_length=30)

	def __str__(self):
		return ('%s')%(self.descripcion)

class TipoAnimal(models.Model):
	descripcion = models.CharField("Tipo de Animal", max_length=30)

	def __str__(self):
		return ('%s')%(self.descripcion)

class TipoMuestra(models.Model):
	descripcion = models.CharField("Tipo de Muestra", max_length=30)

	def __str__(self):
		return ('%s')%(self.descripcion)

class Parametros(models.Model):
	descripcion = models.CharField("Parametro", max_length=30)
	tipo_de_dato_choices = (
		('I', 'Entero'),
		('B', 'Positivo/Negativo'),
		('F', 'Numero con decimales'),
		('S', 'Texto'),
		)
	tipo_de_dato = models.CharField("Tipo de Dato", max_length=1, choices=tipo_de_dato_choices)


	def __str__(self):
		return ('%s')%(self.descripcion)

class Tecnicas(models.Model):
	descripcion = models.CharField("Tecnica", max_length=30)
	parametros = models.ManyToManyField(Parametros)
	tipoMuestra = models.ManyToManyField(TipoMuestra, through='tecXmuestraXanim')

	def __str__(self):
		return ('%s')%(self.descripcion)

class tecXmuestraXanim(models.Model):
	id = models.AutoField(primary_key=True)
	muestra = models.ForeignKey(TipoMuestra)
	tecnica = models.ForeignKey(Tecnicas)
	animal = models. ForeignKey(TipoAnimal)

	class Meta:
		unique_together = ('muestra', 'tecnica', 'animal',)

	def __str__(self):
		return ('%s %s %s')%(self.tecnica, self.muestra, self.animal)

class Motivos(models.Model):
	nombre = models.CharField(max_length=30)
	tercerizacion = models.BooleanField()

	def __str__(self):
		return ('%s')%(self.nombre)

class Individuos(models.Model):
	identificacion = models.CharField("Identificacion / N° de Caravana", max_length=10)
	nombre = models.CharField("Nombre", max_length=15, null=True, blank=True)
	edad = models.CharField("Edad", max_length=2, null=True, blank=True)
	sexo_choices = (
		('M', 'Macho'),
		('H', 'Hembra'),
		('X', 'NS/NC'),
		)
	sexo = models.CharField("Sexo", max_length=1, choices=sexo_choices, null=True, blank=True, default='X')
	obs = models.TextField("Observaciones", null=True, blank=True)

	def __str__(self):
		return ('%s %s %s')%(self.identificacion, self.nombre, self.sexo)

class Establecimiento(models.Model):
	nombre = models.CharField(max_length=50)
	partido = models.CharField(max_length=20)
	propietario = models.CharField(max_length=30)
	RENSPA = models.CharField(max_length=30)
	veterinario = models.ForeignKey(Veterinario, verbose_name="Veterinario de Cabecera")
	hectareas = models.IntegerField("Cant. de Hectareas", null=True, blank=True)
	bovinos = models.IntegerField("Cant. de Hectareas", null=True, blank=True)
	ovinos = models.IntegerField("Cant. de Hectareas", null=True, blank=True)
	categorias = models.ManyToManyField(Categoria)
	explotacion = models.ManyToManyField(Explotacion)

	def __str__(self):
		return ('%s %s')%(self.nombre, self.partido)

class Raza(models.Model):
	nombre = models.CharField(max_length=30)
	tipoAnimal = models.ForeignKey(TipoAnimal)

	def __str__(self):
		return('%s, %s')%(self.nombre, self.tipoAnimal)

class InicioDeCarga(models.Model):
	id = models.AutoField(primary_key=True)
	veterinario = models.ForeignKey(Veterinario)
	establecimiento = models.ForeignKey(Establecimiento)
	motivo = models.ForeignKey(Motivos)
	tipoAnimal = models.ForeignKey(TipoAnimal)
	fecha = models.DateField(auto_now=False)
	cant_indiv = models.IntegerField()
	raza = models.ForeignKey(Raza, null=True, blank=True)
	obs = models.TextField("Observaciones", null=True, blank=True)

	def __str__(self):
		return('%d')%(self.id)

class Protocolo(models.Model):
	numero = models.IntegerField("Numero de Protocolo", primary_key=True)
	tecXmuest = models.ForeignKey(tecXmuestraXanim, verbose_name="Tecnicas")
	inicioCarga = models.ForeignKey(InicioDeCarga, verbose_name="????")
	individuos = models.ManyToManyField(Individuos)
	estado = models.BooleanField("Estado Confirmado")
	obs = models.TextField("Observaciones sobre el Estado")

	def __str__(self):
		return('%d')%(self.numero)
