from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm 
from.models import tblCiente
from django.contrib import messages

# Create your views here.
def inicio(resquest):
    return render (resquest, 'inicio.html')

def quienessomos(resquest):
    return render (resquest, 'quienessomos.html')

def registro(resquest):
    return render (resquest, 'registro.html')

def iniciarsesion(resquest):
    return render (resquest, 'iniciasesion.html')


def adminclientes(request):
    cliente = tblCiente.objects.all()
    return render(request, "adminclientes.html", {"client": cliente})

def registrar(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtapellido']
    telefono = request.POST['numtelefono']
    direccion = request.POST['txtdireccion']
    Email = request.POST['txtemail']
    

    cliens = tblCiente.objects.create(
    apellido=apellido, nombre=nombre,  telefono= telefono,direccion =direccion , Email=Email )
    messages.success(request, '¡registrado!')
    return redirect('/admiClientes/')

def edicioncliente(request, nombre):
    curso = tblCiente.objects.get(codigo=nombre)
    return render(request, "editclientes.html", {"clien": curso})


def editarcliente(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtapellido']
    telefono = request.POST['numtelefono']
    direccion = request.POST['txtdireccion']
    Email = request.POST['txtemail']

    curso = tblCiente.objects.get(nombre=nombre)
    curso.apellido= apellido
    curso.telefono=telefono
    curso.direccion= direccion
    curso.Email=Email
    curso.save()

    messages.success(request, '¡Registro actualizado!')

    return redirect('/admiClientes/')


def eliminarcliente(request, nombre):
    curso = tblCiente.objects.get(nombre=nombre)
    curso.delete()

    messages.success(request, '¡Registro eliminado!')

    return redirect('/admiClientes/')





