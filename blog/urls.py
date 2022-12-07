from django.contrib import admin
from django.urls import path
from .import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('somos/', views.somos, name = 'somos'),
    path ('', views.index, name = 'index'),
    path('publicacion/', include('app.publicacion.urls')),#url de aplicacion de comentarios en publicacion
    
    
]