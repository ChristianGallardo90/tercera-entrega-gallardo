from django.urls import path
from Appcoder.views import inicio, cursos, entregables, estudiantes, profesores, setEstudiantes,getEstudiantes,buscarEstudiante,setCursos,getCursos,buscarCursos,setProfesores,getProfesores,buscarProfesores
urlpatterns = [
    
    path('inicio/', inicio, name="Inicio"),
    path('cursos/', cursos,name="Cursos"),
    path('entregables/', entregables,name="Entregables"),
    path('estudiantes/', estudiantes,name="Estudiantes"),
    path('profesores/', profesores,name="Profesores"),
    path('setEstudiantes/', setEstudiantes,name="setEstudiantes"),
    path('getEstudiantes/', getEstudiantes,name="getEstudiantes"),
    path('buscarEstudiante/', buscarEstudiante,name="buscarEstudiante"),
    path('setCursos/', setCursos,name="setCursos"),
    path('getCursos/', getCursos,name="getCursos"),
    path('buscarCursos/', buscarCursos,name="buscarCursos"),
    path('setProfesores/', setProfesores,name="setProfesores"),
    path('getProfesores/', getProfesores,name="getProfesores"),
    path('buscarProfesores/', buscarProfesores,name="buscarProfesores"),

    
    
    
]
