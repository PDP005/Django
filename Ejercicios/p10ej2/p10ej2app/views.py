from p10ej2app.forms import *
from django.shortcuts import render


def index(request):
    if request.POST:
    #(verifica que tenga contenido)
        form=Formulario(request.POST)
        if form.is_valid():
            collection=form.cleaned_data
            countAficiones=len(collection["aficiones"])
            
            if countAficiones==0:
                mensaje="Eres un soso"
            elif countAficiones==1:
                print(["aficiones"][0])
                mensaje=collection["nombre"]+" deberías buscar más aficiones que "+collection["aficiones"][0]
            elif countAficiones==5:
                mensaje=collection["nombre"]+" creo que tienes demasiadas aficiones"
            else:
                mensaje=""
                
            context={"collection":collection,"mensaje":mensaje}
            
            return render(request,'detalles.html',context)
    else:
        form=Formulario()
    return render(request,"index.html",{'form':form})
