from django.conf.urls import patterns, include, url
from django.contrib import admin
from appgimnasio.views import Index,IngresoCliente,Login,logout_view,informe_ganancias,some_view,IngresoClientesHuella

#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'links', GimnasioViewSet)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gimnasio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^ingreso/$', IngresoCliente.as_view(), name='ingreso'),
    url(r'^ingreso/huella/$', IngresoClientesHuella.as_view(), name='ingreso_huella'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^reporte/$', informe_ganancias, name='reporte'),
    url(r'^pdf/$', some_view, name='some_view'),
    url(r'^admin/', include(admin.site.urls)),
)