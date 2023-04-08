from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Frase, Moderador, Usuario
from django.shortcuts import render, redirect
from inicio.forms import CrearFraseFormulario, BuscarFrases,CrearModeradorFormulario, CrearUsuarioFormulario


def mi_vista(request):
    # print('PASE POR ACA!!!!!')
    # return HttpResponse('<h1>Mi primera vista</h1>')
    return render(request, 'inicio/index.html')

def crear_frase(request):
    
    if request.method == "POST":
        formulario = CrearFraseFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            lafrase = Frase(nombre=datos_correctos['nombre'],edad=datos_correctos['edad'], frase=datos_correctos['frase'],privado=datos_correctos['privado'])
            lafrase.save()

            return redirect('inicio:crear_frase')
    
    formulario = CrearFraseFormulario()
    return render(request, 'inicio/crear_frase.html', {'formulario': formulario})
def crear_usuario(request):
    
    if request.method == "POST":
        formulario = CrearUsuarioFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            elusuario = Usuario(nombre=datos_correctos['nombre'],apellido=datos_correctos['apellido'], inhabilitado=0)
            elusuario.save()

            return redirect('inicio:crear_frase')
    
    formulario = CrearUsuarioFormulario()
    return render(request, 'inicio/crear_usuario.html', {'formulario': formulario})

def crear_moderador(request):
    
    if request.method == "POST":
        formulario = CrearModeradorFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            elmoderador = Moderador(nombre=datos_correctos['nombre'],apellido=datos_correctos['apellido'], fecha_registro=datetime.now())
            elmoderador.save()

            return redirect('inicio:crear_frase')
    
    formulario = CrearModeradorFormulario()
    return render(request, 'inicio/crear_moderador.html', {'formulario': formulario})

def lista_frases(request):
    buscar = request.GET.get('nombre', None)
    
    if buscar:
        mifrases = Frase.objects.filter(nombre__=buscar)
        
    else:
        mifrases = Frase.objects.filter(privado__icontains=0 )
    formulario_busqueda = BuscarFrases()
    return render(request, 'inicio/lista_frases.html', {'frases': mifrases, 'formulario': formulario_busqueda})

    

