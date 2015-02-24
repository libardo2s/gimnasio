from rest_framework import serializers
from appgym.models import Gimnasio

class GimnasioSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Gimnasio
		fields = ('nombre','direccion','telefono','correo','urlfacebook','urltwitter',)
