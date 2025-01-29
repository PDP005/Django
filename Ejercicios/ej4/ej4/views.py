from django.http import HttpResponse
from django.shortcuts import render
from ej4.models.Lenguajes import lenguaje

def inicio(request):
    java:lenguaje=("Java","1234","mola")
    python:lenguaje=("Python","2004","Chuliii")
    l ={java,python}
    
    return render(request,'index.html',l)
#{'nombre':"Java",'año':"1999",'desc':"Mola"}
               