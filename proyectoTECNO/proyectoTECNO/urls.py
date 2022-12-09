"""proyectoTECNO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app_tienda.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('inicio/quienessomos/', quienessomos),
    path('inicio/contactenos/', contactenos),
    path('', login),
    path('cerrarsesion/', logot),
    path('register/', registro),
    path('admclientes/', clientes),
    path('admclientes/eliminar/<id>', elimclientes),
    path('regclientes/', regclientes),
    
    path('admclientes/editclientes/<id>', editclientes),
    path('guarclientes/<id>', guarclientes)

    
    
   
]

