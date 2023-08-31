"""tareas_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from ejercicio1 import views as ej1_views
from ejercicio2 import views as ej2_views
from ejercicio3 import views as ej3_views
from ejercicio4 import views as ej4_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('amigos/',ej1_views.amigos, name="amigos"),
    path('imagenes/',ej2_views.imagenes, name="imagenes"),
    path('calculadora/',ej3_views.calculadora, name="calculadora"),
    path('sopa_letras/',ej4_views.mostrar_sopa_letras, name="sopa_letras")
] 