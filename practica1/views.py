from django.shortcuts import render
from django.http import HttpResponse
from .forms import PracticaForm
from django.shortcuts import render, redirect

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def Home(request):
    return render(request,'Home.html',{
        
    })
    
def Servicios(request):
    return render(request,'Servicios.html',{
        
    })
def contacto(request):
    return render(request,'contacto.html',{
        
    })      
    
def practicas(request):
    if request.method == 'POST':  
        form = PracticaForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('practicas')  
    else:
        form = PracticaForm() 

    return render(request, 'practicas.html', {'form': form})
    
    