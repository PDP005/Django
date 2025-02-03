from django.http import HttpResponse
from django.shortcuts import render
from ej4.models.Lenguajes import lenguaje

def inicio(request):
    java=lenguaje("Java","1234","mola")
    python=lenguaje("Py","12344","Python mola")
    lenguajes={
        java,python
    }
    mensaje=""
    if(len(lenguajes)==0):
        mensaje="Ponte las pilas"
    if(len(lenguajes)==1):
        mensaje="estas empezando"
    #cuando se pasa algo siempre se pasa un diccionario nunca un objeto solo 
    return render(request,'index.html',{'l':lenguajes,'mensaje':mensaje})
               