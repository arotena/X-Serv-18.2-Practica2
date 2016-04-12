from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from models import Page
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def redirigir(request, key):
    try:
        valor = Page.objects.get(id=key)
        respuesta = "<html><head><meta http-equiv='refresh' content='1;"
        respuesta += "url=" + valor.url_original
        respuesta += "'></head>" + "<body></body></html>\r\n"
    except Page.DoesNotExist:
        respuesta = "Esta id no existe"
    return HttpResponse(respuesta)

def procUrl(url):
        if("http://" in url):
            partido = url.split("http://")[1]
            valor_guardar = "http://" + partido
        elif("https://" in url):
            partido = url.split("https://")[1]
            valor_guardar = "https://" + partido
        else:
            valor_guardar = "http://" + url
        return valor_guardar

@csrf_exempt
def inicio(request):
    if request.method == "POST":
        url = request.POST.get('url')
        url = procUrl(url);
        try:
            encontrada = Page.objects.get(url_original=url)
        except Page.DoesNotExist:
            pag = Page(url_original=url)
            pag.save()
            encontrada = Page.objects.get(url_original=url)
        return HttpResponse("http://localhost:1234/" + str(encontrada.id))
    listado = Page.objects.all()
    respuesta = "<ol>"
    for elemento in listado:
        respuesta += '<li><a href ="'+ str(elemento.url_original) + '">'
        respuesta += str(elemento.url_original) + '</a>' + " = "
        respuesta += '<a href="'+ str(elemento.id) +'">'
        respuesta += "http://localhost:1234/" + str(elemento.id) + '</a>'
    respuesta += "</ol>"
    template = get_template("pag.html")
    argumentos = {'contenido': respuesta,}
    return HttpResponse(template.render(Context(argumentos)))
def notFound(request):
    return HttpResponse("Not Found: Argumentos invalidos")
