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

def editclientes(request, id):
    cliente=tblCiente.objects.get(id=id)
    
    return render(request, 'editclientes.html', {"clien":cliente})

def guarclientes(request, id):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtapellido']
    telefono = request.POST['numtelefono']
    direccion = request.POST['txtdireccion']
    Email = request.POST['txtemail']
    
    id=tblCiente.objects.get(id=id)
    id.nombre=nombre
    id.apellido=apellido
    id.telefono=telefono
    id.direccion=direccion
    id.Email=Email
    id.save()
    
    messages.success(request, '¡Curso actualizado!')

    return redirect('/admiClientes/')


def elimclientes(request,id):
    cliente=tblCiente.objects.get(id=id)
    cliente.delete()
    return redirect('/admiClientes/')





