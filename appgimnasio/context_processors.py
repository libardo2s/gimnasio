# -*- encoding: utf-8 -*-
from .models import Gimnasio

def info_gym(request):
	try:
		gimnasio=Gimnasio.objects.get(codigo='G0001')
		return {'gimnasio':gimnasio}
	except Gimnasio.DoesNotExist:
		gimnasio = Gimnasio.objects.create(codigo="G0001",nombre="Sin Nombre",direccion="Sin Direccion",telefono="0000000000",correo="zzzz@zzzz.zzz",urlfacebook = "https://www.facebook.com/",urltwitter = "https://twitter.com/")
		gimnasio.save()
		return {'gimnasio':gimnasio}