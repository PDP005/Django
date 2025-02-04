from ej6.models.Asignatura import asignatura
from django.shortcuts import render

def inicio(request):
    java=asignatura("Java","1234","mola")
    python=asignatura("Py","12344","Python mola")
    asig={
        java,python
    }
    return render(request,'index.html',{'asignaturas':asig})


