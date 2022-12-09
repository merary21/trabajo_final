from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def inicio(resquest):
    return render (resquest, 'inicio.html')

def quienessomos(resquest):
    return render (resquest, 'quienessomos.html')

def contactenos(resquest):
    return render (resquest, 'contacto.html')

def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
         login(request, user)
        return redirect('inicio/')
    return render(request, "lte.html")

def logot(request):
    logout(request)
    return redirect("/")


class Registro(UserCreationForm):
    class Meta:
        model = User 
        fields=['username','password1','password2','email','first_name','last_name']

    
def registro(request):
    form=Registro()
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
           form.save()
          
    return render(request, "register.html", {"form":form})

def clientes(request):
    cliente = tblCiente.objects.all()
    return render(request, "clientes.html", {"cliente":cliente})

def regclientes(request):
   nombre=request.POST['name1']
   apellido=request.POST['ape1']
   telefono=request.POST['tfno1']
   direccion=request.POST['dic1']
   Email=request.POST['ema1']
   cliente=tblCiente.objects.create(
    nombre=nombre, apellido=apellido, telefono=telefono, direccion=direccion, Email=Email
   )
   
   messages.success(request, '¡Cliente Registrado!')

   return redirect('/clientes')

def aggpedido(request):
    cantidad=request.POST['num']
    precio=request.POST['pre']
    pedido= tblpedido.objects.create(
    cantidad=cantidad, precio=precio)

    

    return redirect('/pedidos')

def editclientes(request, id):
    cliente=tblCiente.objects.get(id=id)
    
    return render(request, 'editcliente.html', {"cliente":cliente})

def guarclientes(request, id):
   nombre=request.POST['name1']
   apellido=request.POST['ape1']
   telefono=request.POST['tfno1']
   direccion=request.POST['dic1']
   Email=request.POST['ema1']
   id=tblCiente.objects.get(id=id)
   id.nombre=nombre
   id.apellido=apellido
   id.telefono=telefono
   id.direccion=direccion
   id.Email=Email
   id.save()
   
   messages.success(request, '¡Registro actualizado!')

   return redirect('/clientes')

def elimclientes(request,id):
    cliente=tblCiente.objects.get(id=id)
    cliente.delete()
    
    messages.success(request, '¡Cliente eliminado!')
    
    return redirect('/clientes')

def pedido(request):
    pedido = tblpedido.objects.all()

    return render (request, 'pedidos.html', {"pedido":pedido})

def registrarped (request):

    return HttpResponse 


