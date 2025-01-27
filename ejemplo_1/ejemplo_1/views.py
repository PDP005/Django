from django.http import HttpResponse
from django.shortcuts import render

def saluda(request):
    #return HttpResponse("hola daw 2")
    contexto ={'nombre':"Pedro",
               'mensaje':"Holaa mensaje",
               'l':['l','q','w','e']
               }
    return render(request,'index.html',contexto)
def despedida(request):
    return render(request,'salir.html')
def tuEdadFutura(request,e):
    e+=10
    contexto={
        'edad':e
    }
    return render(request,'index.html',contexto)