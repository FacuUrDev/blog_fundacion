from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('lista/',views.lista_de_noticias,name='lista_de_noticias'),
    path('detalles/',views.detalle_de_noticia,name='detalle_de_noticia'),
    path('nueva/',views.nueva_noticia,name='nueva_noticia'),
    path('comentarios/', views.comentarios, name='comentarios'),
    

]