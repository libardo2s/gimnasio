from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
#from rest_framework import viewsets
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import FormView
from appgimnasio.models import Servicio, Gimnasio, Cliente, HistorialIngresoCliente, Gasto, Ingreso
from appgimnasio.forms import IngresoUsuario, LoginUsuario
#from appgimnasio.serializers import GimnasioSerializers
#import datetime
from django.utils import timezone

# Create your views here.
class Index(ListView):
	template_name = "index.html"
	model = Servicio
	context_object_name = "servicios"

class IngresoCliente(FormView):
	template_name = "ingreso_clientes.html"
	form_class = IngresoUsuario
	success_url = reverse_lazy('index')

	def form_valid(self, form):
		try:
			cliente = Cliente.objects.get(identificacion = form.cleaned_data['identificacion'])
			historial = HistorialIngresoCliente(idCliente = cliente)
			historial.save()
			return super(IngresoCliente, self).form_valid(form)
		except Cliente.DoesNotExist:
			return render_to_response('ingreso_clientes.html',{"estado":"No Registrado","form":form},context_instance=RequestContext(self.request))

class Login(FormView):
	template_name = "login_usuario.html"
	form_class = LoginUsuario
	success_url = reverse_lazy('index')

	def form_valid(self, form):
		usr = form.cleaned_data['usuario']
		psw = form.cleaned_data['contrasena']
		autenticacion = authenticate(username=usr, password=psw)
		if autenticacion is not None:
			if autenticacion.is_active:
				login(self.request,autenticacion)
				return redirect(reverse_lazy('index'))
			else:
				return render_to_response('login_usuario.html',{"estado":"Error de Usuario o Contrasena","form":form},context_instance=RequestContext(self.request))
		else:
			return render_to_response('login_usuario.html',{"estado":"Error de Usuario o Contrasena","form":form},context_instance=RequestContext(self.request))
		return super(Login, self).form_valid(form)

def informe_ganancias(request):
	fecha_reporte = timezone.now()
	ingresos = Ingreso.objects.filter(fecha=fecha_reporte)
	suma_ingresos = 0
	for i in ingresos:
		suma_ingresos  = suma_ingresos + i.monto

	gastos = Gasto.objects.filter(fecha=fecha_reporte)
	suma_gastos = 0
	for g in gastos:
		suma_gastos = suma_gastos + g.monto

	total = suma_ingresos - suma_gastos
	return render_to_response('reporte_ganancias.html',locals(),context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('index'))

"""class GimnasioViewSet(viewsets.ModelViewSet):
	queryset = Gimnasio.objects.all()
	serializer_class = GimnasioSerializers"""