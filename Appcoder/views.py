from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Estudiante,Curso,Profesor
from Appcoder.forms import formSetEstudiante,formSetCursos,formSetProfesor
# Create your views here.


def inicio(request):
     return render(request,"AppCoder/inicio.html")

def cursos(request):
    return render(request,"AppCoder/cursos.html")

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")

def setEstudiantes(request):
    if request.method == 'POST':
        miFormulario = formSetEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            estudiantes = Estudiante(nombre=data["nombre"],apellido=data["apellido"],email=data["email"])
            estudiantes.save()
            return render(request,"AppCoder/inicio.html")

    else:
        miFormulario = formSetEstudiante
    return render(request,"AppCoder/setEstudiantes.html",{"miFormulario":miFormulario})

def getEstudiantes(request):
    return render(request,"AppCoder/getEstudiantes.html")

def buscarEstudiante(request):
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         estudiantes = Estudiante.objects.filter(nombre = nombre)
         return render(request,"AppCoder/getEstudiantes.html",{"estudiantes":estudiantes})
    else:
        respuesta = "no se enviaron datos"
    return HttpResponse(respuesta)

def setCursos(request):
    if request.method == 'POST':
        miFormulario = formSetCursos(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            cursos = Curso(nombre=data["nombre"],camada=data["camada"])
            cursos.save()
            return render(request,"AppCoder/inicio.html")
    else:
          miFormulario = formSetCursos
    return render(request,"AppCoder/setCursos.html",{"miFormulario":miFormulario})      

def getCursos(request):
    return render(request,"AppCoder/getCursos.html")   

def buscarCursos(request):
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         cursos = Curso.objects.filter(nombre = nombre)
         return render(request,"AppCoder/getCursos.html",{"cursos":cursos})
    else:
        respuesta = "no se enviaron datos"
    return HttpResponse(respuesta)     

def setProfesores(request):
    if request.method == 'POST':
        miFormulario = formSetProfesor(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesores = Profesor(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],profesion=data["profesion"])
            profesores.save()
            return render(request,"AppCoder/inicio.html")
    else:
          miFormulario = formSetProfesor
    return render(request,"AppCoder/setProfesores.html",{"miFormulario":miFormulario})  

def getProfesores(request):
    return render(request,"AppCoder/getProfesores.html")  

def buscarProfesores(request):
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         profesores = Profesor.objects.filter(nombre = nombre)
         return render(request,"AppCoder/getProfesores.html",{"profesores":profesores})
    else:
        respuesta = "no se enviaron datos"
    return HttpResponse(respuesta)     
  
