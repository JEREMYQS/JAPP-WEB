from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def Home(request):
    return render(request,'Home.html',{
        
    })
    
def Servicios(request):
    return render(request,'Servicios.html',{
        
    })
