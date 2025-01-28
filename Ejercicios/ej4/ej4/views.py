from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    l =[{'nombre':"Java",
               'año':"1999",
               'desc':"Mola"
               },{'nombre':"Python",
               'año':"2004",
               'desc':"Chuliii"
               }]
    
    return render(request,'index.html',l)