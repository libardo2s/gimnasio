from django.contrib import admin
from appgimnasio.models import Cliente,Empleado,ConceptoIngreso,ConceptoGasto,Gasto,Ingreso,Servicio,Gimnasio,HistorialIngresoCliente
# Register your models here.

class HistorialAdmin(admin.ModelAdmin):
	list_display = ('idCliente', 'fecha')
	readonly_fields = ('fecha',)

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('identificacion','nombre','segundoNombre','apellido','segundoApellido','fechaNacimiento','telefono',) 
	search_fields = ('identificacion', 'nombre',)

class GastoAdmin(admin.ModelAdmin):
	list_display = ('fecha','concepto','monto',)
	readonly_fields = ('fecha',)

class IngresoAdmin(admin.ModelAdmin):
	list_display = ('fecha','concepto','monto',)
	readonly_fields = ('fecha',)

class GimnasioAdmin(admin.ModelAdmin):
	list_display = ('nombre','direccion','telefono','correo','urlfacebook','urltwitter',)

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Empleado)
admin.site.register(ConceptoIngreso)
admin.site.register(ConceptoGasto)
admin.site.register(Gasto,GastoAdmin)
admin.site.register(Ingreso,IngresoAdmin)
admin.site.register(Servicio)
admin.site.register(Gimnasio,GimnasioAdmin)
admin.site.register(HistorialIngresoCliente,HistorialAdmin)