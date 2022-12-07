from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
  nombre = models.CharField(max_length=100)

class Noticia(models.Model):
  titulo = models.CharField(max_length=100)
  contenido = models.TextField()
  fecha_publicacion = models.DateTimeField(auto_now_add=True)
  autor = models.ForeignKey(User, on_delete=models.CASCADE)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Comentario(models.Model):
  noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
  contenido = models.TextField()
  fecha_publicacion = models.DateTimeField(auto_now_add=True)
  autor = models.ForeignKey(User, on_delete=models.CASCADE)