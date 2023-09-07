from django.http import HttpResponse
import bluetooth as bt
from django.shortcuts import render
from app.models import dispositivo

# Create your views here.


# Creamos variables para almacenar direcciones y nombres por separado
# pero de manera ordenada
'''
def detectar():
    ## Descubrimos los dispositivos cercanos 
    nearby_devices = bt.discover_devices(lookup_names=True)
    # Creamos un vector para almacenar los dispositivos encontrados
    dispositivos = []
    # Agregamos cada dispositivo a mod de diccionario por nombre y MAC
    for addr, name in nearby_devices:
        dispositivos.append({
            "nombre": name,
            "MAC": addr
        })
    return dispositivos
'''

# ahora vamos añadiendo los datos a la base de datos

'''
for d in detectar():
    disp = dispositivo(nombre=d["nombre"], MAC=d["MAC"])
    disp.save()
'''

def showDisp(request):
    title = "PROYECTO DE SISTEMAS INALÁMBRICOS"
    dps = dispositivo.objects.all()
    length =len(dispositivo.objects.all())
    return render(request,'disp.html',{
        'title':title,
        'dps': dps,
        'largo' : length
    })

def hello(request):
    return render(request, 'index.html')


    
