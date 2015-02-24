from django.db import models

# Create your models here.
class Cliente(models.Model):
	identificacion = models.IntegerField('Numero de Documento', primary_key=True)
	nombre = models.CharField('Primer Nombre', max_length='50')
	segundoNombre = models.CharField('Segundo Nombre', max_length='50', null=True)
	apellido = models.CharField('Primer Apellido', max_length='50')
	segundoApellido = models.CharField('Segundo Apellido', max_length='50', null=True)
	fechaNacimiento = models.DateField('Fecha de Nacimiento')
	telefono = models.CharField('Telefono', max_length='10')

	def __unicode__(self):
		return	'%s %s' %(self.nombre,self.apellido)

class HistorialIngresoCliente(models.Model):
	idCliente = models.ForeignKey(Cliente)
	fecha = models.DateTimeField('Fecha')

	def __unicode__(self):
		return self.idCliente.nombre

class Empleado(models.Model):
	identificacion = models.IntegerField('Numero de Documento', primary_key=True, max_length='20')
	nombre = models.CharField('Primer Nombre', max_length='50')
	segundoNombre = models.CharField('Segundo Nombre', max_length='50', null=True)
	apellido = models.CharField('Primer Apellido', max_length='50')
	segundoApellido = models.CharField('Segundo Apellido', max_length='50', null=True)

	def __unicode__(self):
		return "%s %s" %(self.nombre,self.apellido)

class ConceptoIngreso(models.Model):
	codigo = models.CharField('Codigo', max_length='5',primary_key=True)
	nombre = models.CharField('Nombre del Concepto', max_length='30')

	def __unicode__(self):
		return self.nombre

class ConceptoGasto(models.Model):
	codigo = models.CharField('Codigo', max_length='5',primary_key=True)
	nombre = models.CharField('Nombre del Concepto', max_length='30')

	def __unicode__(self):
		return self.nombre

class Gasto(models.Model):
	codigo = models.CharField('Codigo', max_length='5',primary_key=True)
	concepto = models.ForeignKey('ConceptoGasto')
	fecha = models.DateField('Fecha', auto_now=True)
	monto = models.IntegerField(max_length='6')

	def __unicode__(self):
		return "%s %s"% (self.fecha,self.concepto.nombre)

class Ingreso(models.Model):
	codigo = models.CharField('Codigo', max_length='5',primary_key=True)
	concepto = models.ForeignKey('ConceptoIngreso')
	fecha = models.DateField('Fecha', auto_now=True)
	monto = models.IntegerField(max_length='6')

	def __unicode__(self):
		return "%s %s"% (self.fecha,self.concepto.nombre)

class Servicio(models.Model):
	codigo = models.CharField('Codigo', max_length='5', primary_key=True)
	servicio = models.CharField("Servicio", max_length=50)
	tarifa = models.IntegerField(max_length='6')

	def __unicode__(self):
		return self.servicio

class Gimnasio(models.Model):
	codigo = models.CharField('Codigo', max_length='5', primary_key=True)
	nombre = models.CharField('Nombre Gimnasio', max_length='70')
	direccion = models.CharField('Direccion', max_length='30')
	telefono = models.CharField('Telefono', max_length='10')
	correo = models.EmailField()
	urlfacebook = models.URLField(blank=True,null=True)
	urltwitter = models.URLField(blank=True,null=True)

	def  __unicode__(self):
	    return self.nombre