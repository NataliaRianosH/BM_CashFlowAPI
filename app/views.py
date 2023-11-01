from django.shortcuts import render , redirect
from .models import ConceptoGasto
from rest_framework.decorators import api_view, action
from rest_framework import generics, viewsets, status
from .serializers import ConceptoGastoSerializer

def concepto_gastos(request):
    conceptos= ConceptoGasto.objects.all()
    print(conceptos)
    return render(request, 'newConceptoDeGasto.html', {"conceptos": conceptos})

def crear_concepto_gastos(request):
    print(request.POST)
    concepto = ConceptoGasto(nombre_concepto=request.POST['nombre'], descripcion=request.POST['descripcion'], estado=request.POST['estado'] )
    concepto.save()
    return redirect('/app/')

def eliminar_concepto_gasto(request, concepto_id):
   
    conceptoGasto = ConceptoGasto.objects.get(id = concepto_id)
    #print(conceptoGasto)
    conceptoGasto.delete()
    return redirect('/app/')

def modificar_concepto(request, concepto_id):
    if request.method == 'POST':
        concepto = ConceptoGasto.objects.get(id=concepto_id)
        concepto.nombre_concepto = request.POST['nombre']
        concepto.estado = request.POST['estado']
        concepto.descripcion = request.POST['descripcion']
        concepto.save()

    return redirect('/app/')

class ConceptoGastosViewSet(viewsets.ModelViewSet):
    queryset = ConceptoGasto.objects.all()
    serializer_class = ConceptoGastoSerializer