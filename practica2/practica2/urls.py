
from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'procesar.views.inicio'),
    url(r'^(\d)+$', 'procesar.views.redirigir'),
    url(r'.*' , 'procesar.views.notFound')
]
