from django.shortcuts import render , redirect
from .models import ConceptoGasto

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

