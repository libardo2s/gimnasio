from django.contrib import admin
from appgimnasio.models import Cliente,Empleado,ConceptoIngreso,ConceptoGasto,Gasto,Ingreso,Servicio,Gimnasio,HistorialIngresoCliente
# Register your models here.

class HistorialAdmin(admin.ModelAdmin):
	list_display = ('idCliente', 'fecha')
	
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(ConceptoIngreso)
admin.site.register(ConceptoGasto)
admin.site.register(Gasto)
admin.site.register(Ingreso)
admin.site.register(Servicio)
admin.site.register(Gimnasio)
admin.site.register(HistorialIngresoCliente,HistorialAdmin)