from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Comentario

from .models import Noticia, Categoria
from .forms import NoticiaForm

def lista_de_noticias(request):
  noticias = Noticia.objects.all()
  return render(request, "blog/noticias.html", {"noticias": noticias})

def detalle_de_noticia(request, id):
  noticia = Noticia.objects.get(id=id)
  return render(request, "blog/noticia.html", {"noticia": noticia})

def nueva_noticia(request):
  if request.method == "POST":
    form = NoticiaForm(request.POST)
    if form.is_valid():
      noticia = form.save(commit=False)
      noticia.autor = request.user
      noticia.save()
      return redirect("detalle_de_noticia", id=noticia.id)
  else:
    form = NoticiaForm()
  return render(request, "blog/nueva_noticia.html", {"form": form})


def comentarios(request):
  # Obtener todos los comentarios de la base de datos
  comentarios = Comentario.objects.all()

  # Crear una cadena de texto con los datos de cada comentario
  comentarios_str = ""
  for comentario in comentarios:
    comentarios_str += f"{comentario.contenido} - {comentario.autor}\n"

  # Devolver una respuesta HTTP con la lista de comentarios
  return HttpResponse(comentarios_str)