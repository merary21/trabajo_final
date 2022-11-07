from django.shortcuts import render

# Create your views here.
def inicio(resquest):
    return render (resquest, 'inicio.html')

def quienessomos(resquest):
    return render (resquest, 'quienessomos.html')
