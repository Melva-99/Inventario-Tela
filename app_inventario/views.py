from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib import messages

#PARA GENERAR PDF
from .utils import render_to_pdf
from django.views.generic import View


#INICIO
@login_required()
def index(request):
    return render(request, 'inventario/index.html')

#INVENTARIO
@login_required()
def inventario(request):
    inventarioTela = Inventario.objects.all()
    tela = Tela.objects.all()
    
    ctx = {
        'inventarioTela': inventarioTela,
        'tela': tela,
    }

    return render(request, 'inventario/inventario.html',ctx)

#SALIDA
@login_required()
def salida(request):

    q = request.GET.get('q')

    if q:
        inventario = Inventario.objects.filter(tela__nombre__icontains=q)
    else:
        inventario = Inventario.objects.all()
    ctx ={
        'inv' : inventario,
    }
    return render(request, 'inventario/salida.html', ctx)

@login_required()
def salidaTelas(request, id, id_estante):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        diseno = request.POST.get('diseno')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = request.POST.get('numeroRollo')
        cantidadYarda = float(request.POST.get('cantidad'))
        estante = request.POST.get('estante')

    dicti ={'t': id, 'e': id_estante}
    it = get_object_or_404(Inventario, tela=dicti.get('t'),estante=dicti.get('e'))
    t = Tela.objects.get(pk=dicti.get('t'))
    if request.method == 'POST':
        add_stock = float(request.POST.get('cantidad'))

        if it.cantidadYarda  >= 1 and  add_stock <= it.cantidadYarda:
            detalleSalida = DetalleSalida(nombre=nombre, diseno=diseno, calidad=calidad, color=color, numeroRollo=numeroRollo, cantidadYarda=cantidadYarda, estante=estante)
            it.cantidadYarda -= add_stock
            it.save()
            detalleSalida.save()
            msj = 'Salida exitosamente'
            messages.add_message(request,messages.INFO, msj)
            
        else:
            msj = 'Cantidad insuficiente en stock'
            messages.add_message(request,messages.INFO, msj)

        telas = Tela.objects.all().order_by('nombre')
        inv = Inventario.objects.all()
        ctx ={
                'inv' : inv,
                'telas': telas,
                'msj':'success',
            }
        return render(request, 'inventario/salida.html', ctx)

    data = Tela.objects.all().order_by('nombre')
    inv = Inventario.objects.all()
    ctx = {
        'telas': data,
        't': t,
        'inv' : inv,
        'it' : it,
    }
    return render(request, 'inventario/salida.html', ctx)

#ENTRADA
@login_required()
def entrada(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = int(request.POST.get('numeroRollo'))
        cantidadYarda = float(request.POST.get('cantidadYarda'))
        fecha = request.POST.get('fecha')
        diseno = int(request.POST.get('diseno'))
        IdEstante = int(request.POST.get('estante'))
        estante = Estante.objects.get(pk=IdEstante)

        p = Tela(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, diseno=diseno)
        p.save()
        
        telasInv = Tela.objects.last()

        inv = Inventario(estante=estante,tela=telasInv, diseno=diseno, cantidadYarda=cantidadYarda, fecha=fecha)
        inv.save()
        p.save()

        msj = 'Tela registrada correctamente.'
        messages.add_message(request, messages.INFO, msj)

    telas = Tela.objects.all().order_by('nombre')
    inventario = Inventario.objects.all()

    ctx ={
        'telas': telas,
        'estante': Estante.objects.all(),
        'msj':'success',
        'inventario': inventario,
    }
    return render(request, 'inventario/entrada.html', ctx)

@login_required()
def detalleSalida(request):
    detalleSalida = DetalleSalida.objects.all()

    ctx = {
        'detalleSalida': detalleSalida
    }
    return render(request, 'inventario/detalleSalida.html',ctx)


class salidaPdf(View):
    def get(self, request, *args, **kwargs):
        Salida = DetalleSalida.objects.all()
        
        ctx = {
            'Salida': Salida.last(),
        }
        pdf = render_to_pdf('inventario/salidaPdf.html', ctx)
        return HttpResponse(pdf, content_type='application/pdf')