from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView
from appgimnasio.models import Servicio, Gimnasio, Cliente, HistorialIngresoCliente, Gasto, Ingreso
from appgimnasio.forms import IngresoUsuario, LoginUsuario
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from django.http import HttpResponse
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

class IngresoClientesHuella(TemplateView):
	template_name = "ingreso_usuario_huella.html"


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

@login_required(login_url=reverse_lazy('login'))
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

	#total = suma_ingresos - suma_gastos
	return render_to_response('reporte_ganancias.html',locals(),context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('index'))

def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    hora = timezone.now()

    ingresos = Ingreso.objects.filter(fecha=hora)
    suma_ingresos = 0
    for i in ingresos:
    	suma_ingresos  = suma_ingresos + i.monto
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(500, 500,"%s"%(hora))
    p.drawString(400, 400,"total ingresos %s"%(suma_ingresos))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response