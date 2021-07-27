from django.shortcuts import render
from .models import TipoNoticia, Noticia

def caos(request):
    contexto = {"nombre ":"Samuel"}
    return render(request, "core/caos.html",contexto)

def galeria(request):
    noticias = Noticia.objects.all()
    contexto = {"noticias ":noticias}
    return render(request, "core/galeria.html",contexto)

def formulario(request):
    return render(request, "core/formulario.html")

def registro(request):
    tipos = TipoNoticia.objects.all() 
    contexto = {"tipos":tipos}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        desc = request.POST.get("txtDesc")
        tipo = request.POST.get("cboTipo")
        imagen = request.FILES.get("txtImg")
        obj_tipo = TipoNoticia.objects.get(nombre=tipo) 
        mas = Noticia(
            nombre=nombre,
            descripcion=desc,
            imagen=imagen,
            tipo=obj_tipo
        )
        mas.save()
        contexto = {"tipos":tipos,"mensaje":"grabo"}
    return render(request, "core/registro.html",contexto)

