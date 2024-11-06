from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')
def doctores(request):
    return render(request,'doctores/index.html')
def crear(request):
    return render(request,'doctores/crear.html')
def editar(request):
    return render(request,'doctores/editar.html')