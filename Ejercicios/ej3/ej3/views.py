from django.http import HttpResponse
from django.shortcuts import render
#from ej3.models import fecha
from datetime import datetime


def inicio(request):
    hoy= datetime.now()
    pasar={
        hoy
    }
    return render(request,'index.html',pasar)
