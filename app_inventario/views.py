from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect, reverse
from .models import *
from django.db import transaction
from django.contrib import messages

#INICIO
def index(request):
    return render(request, 'inventario/index.html')

#ESTANTE 1
def inventarioE1(request):
    inventarioTela = Inventario.objects.filter(estante=1)
    tela = Tela.objects.all()
    
    ctx = {
        'inventarioTela': inventarioTela,
        'tela': tela,
    }

    return render(request, 'inventario/Estante1/inventarioE1.html',ctx)

def salidaE1(request):
    inventario = Inventario.objects.filter(estante=1)
    tela = Tela.objects.all()
    ctx ={
        'tela': tela,
        'inv' : inventario,
    }
    return render(request, 'inventario/Estante1/salidaE1.html', ctx)

def salidaTelas(request, id, id_estante):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = request.POST.get('numeroRollo')
        cantidadYarda = request.POST.get('cantidad')
        
        idEst = Estante.objects.get(pk=1)
        ds = DetalleSalida(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, cantidadYarda=cantidadYarda, estante=idEst)
        ds.save()

    dicti ={'t': id, 'e': id_estante}
    it = get_object_or_404(Inventario, tela=dicti.get('t'))
    t = Tela.objects.get(pk=dicti.get('t'))
    if request.method == 'POST':
        add_stock = int(request.POST.get('cantidad'))

        if it.cantidadYarda  >= 1 and  add_stock <= it.cantidadYarda:
            it.cantidadYarda -= add_stock
            it.save()
            
        else:
            msj = 'Cantidad insuficiente en stock'
            messages.add_message(request,messages.INFO, msj)
            
        telas = Tela.objects.all().order_by('nombre')
        inv = Inventario.objects.filter(estante=1)
        ctx ={
                'inv' : inv,
                'telas': telas,
                'msj':'success',
            }
        return render(request, 'inventario/Estante1/salidaE1.html', ctx)
    
    data = Tela.objects.all().order_by('nombre')
    inv = Inventario.objects.filter(estante=1)
    ctx = {
        'telas': data,
        't': t,
        'inv' : inv,
        'it' : it,
    }
    return render(request, 'inventario/Estante1/salidaE1.html', ctx)

def entradaE1(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = int(request.POST.get('numeroRollo'))
        cantidadYarda = int(request.POST.get('cantidadYarda'))
        IdTela = int(request.POST.get('tipoTela'))
        tipoTela = Tipo_Tela.objects.get(pk=IdTela)
        
        try:
            tela = Tela.objects.get(nombre=nombre)
        except:
            pass
        
        variable = ''
        try:
            variable = Inventario.objects.get(tela=tela)
            
        except:
            pass

        if Tela.objects.filter(nombre=nombre) and variable != '':

            data = Tela.objects.all().order_by('nombre')
            inventario = Inventario.objects.all()
            ctx = {
                'tela': data,
                'msj':'danger',
                'inventario' : inventario
            }
            msj = 'La tela ya existe!'
            messages.add_message(request,messages.INFO, msj)
            return render(request, 'inventario/Estante1/entradaE1.html', ctx)

        try:
            telas
        except:
            p = Tela(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, tipoTela=tipoTela)
            p.save()
            
        telasInv = Tela.objects.get(nombre=nombre)
        idEst = Estante.objects.get(pk=1)
        inv = Inventario(estante=idEst,tela=telasInv, cantidadYarda=cantidadYarda)
        inv.save()

        msj = 'Tela registrada correctamente.'
        messages.add_message(request, messages.INFO, msj)
        
        data = Tela.objects.all().order_by('nombre')
        inventario = Inventario.objects.all()
        ctx = {
            'telas': data,
            'tipoTela': Tipo_Tela.objects.all(),
            'msj':'success',
            'inventario' : inventario
        }
        
        return render(request, 'inventario/Estante1/entradaE1.html', ctx)

    telas = Tela.objects.all().order_by('nombre')
    inventario = Inventario.objects.all()

    ctx ={
        'telas': telas,
        'tipoTela': Tipo_Tela.objects.all(),
        'inventario': inventario,
    }
    return render(request, 'inventario/Estante1/entradaE1.html', ctx)

#ESTANTE 2
def inventarioE2(request):
    inventarioTela = Inventario.objects.filter(estante=2)
    tela = Tela.objects.all()
    
    ctx = {
        'inventarioTela': inventarioTela,
        'tela': tela,
    }

    return render(request, 'inventario/Estante2/inventarioE1.html',ctx)

def salidaE2(request):
    inventario = Inventario.objects.filter(estante=2)
    tela = Tela.objects.all()
    ctx ={
        'tela': tela,
        'inv' : inventario,
    }
    return render(request, 'inventario/Estante2/salidaE1.html', ctx)

def salidaTelas2(request, id, id_estante):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = request.POST.get('numeroRollo')
        cantidadYarda = request.POST.get('cantidad')
        
        idEst = Estante.objects.get(pk=2)
        ds = DetalleSalida(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, cantidadYarda=cantidadYarda, estante=idEst)
        ds.save()

    dicti ={'t': id, 'e': id_estante}
    it = get_object_or_404(Inventario, tela=dicti.get('t'))
    t = Tela.objects.get(pk=dicti.get('t'))
    if request.method == 'POST':
        add_stock = int(request.POST.get('cantidad'))

        if it.cantidadYarda  >= 1 and  add_stock <= it.cantidadYarda:
            it.cantidadYarda -= add_stock
            it.save()
            
        else:
            msj = 'Cantidad insuficiente en stock'
            messages.add_message(request,messages.INFO, msj)
            
        telas = Tela.objects.all().order_by('nombre')
        inv = Inventario.objects.filter(estante=2)
        ctx ={
                'inv' : inv,
                'telas': telas,
                'msj':'success',
            }
        return render(request, 'inventario/Estante2/salidaE1.html', ctx)
    
    data = Tela.objects.all().order_by('nombre')
    inv = Inventario.objects.filter(estante=2)
    ctx = {
        'telas': data,
        't': t,
        'inv' : inv,
        'it' : it,
    }
    return render(request, 'inventario/Estante2/salidaE1.html', ctx)

def entradaE2(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = int(request.POST.get('numeroRollo'))
        cantidadYarda = int(request.POST.get('cantidadYarda'))
        IdTela = int(request.POST.get('tipoTela'))
        tipoTela = Tipo_Tela.objects.get(pk=IdTela)
        
        try:
            tela = Tela.objects.get(nombre=nombre)
        except:
            pass
        
        variable = ''
        try:
            variable = Inventario.objects.get(tela=tela)
            
        except:
            pass

        if Tela.objects.filter(nombre=nombre) and variable != '':
            data = Tela.objects.all().order_by('nombre')
            inventario = Inventario.objects.all()
            ctx = {
                'tela': data,
                'msj':'danger',
                'inventario' : inventario
            }
            msj = 'La tela ya existe!'
            messages.add_message(request,messages.INFO, msj)
            return render(request, 'inventario/Estante2/entradaE1.html', ctx)

        try:
            telas
        except:
            p = Tela(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, tipoTela=tipoTela)
            p.save()
            
        telasInv = Tela.objects.get(nombre=nombre)
        idEst = Estante.objects.get(pk=2)
        inv = Inventario(estante=idEst,tela=telasInv, cantidadYarda=cantidadYarda)
        inv.save()

        msj = 'Tela registrada correctamente.'
        messages.add_message(request, messages.INFO, msj)
        
        data = Tela.objects.all().order_by('nombre')
        inventario = Inventario.objects.all()
        ctx = {
            'telas': data,
            'tipoTela': Tipo_Tela.objects.all(),
            'msj':'success',
            'inventario' : inventario
        }
        
        return render(request, 'inventario/Estante2/entradaE1.html', ctx)

    telas = Tela.objects.all().order_by('nombre')
    inventario = Inventario.objects.all()

    ctx ={
        'telas': telas,
        'tipoTela': Tipo_Tela.objects.all(),
        'inventario': inventario,
    }
    return render(request, 'inventario/Estante2/entradaE1.html', ctx)

#ESTANTE 3
def inventarioE3(request):
    inventarioTela = Inventario.objects.filter(estante=3)
    tela = Tela.objects.all()
    
    ctx = {
        'inventarioTela': inventarioTela,
        'tela': tela,
    }

    return render(request, 'inventario/Estante3/inventarioE1.html',ctx)

def salidaE3(request):
    inventario = Inventario.objects.filter(estante=3)
    tela = Tela.objects.all()
    ctx ={
        'tela': tela,
        'inv' : inventario,
    }
    return render(request, 'inventario/Estante3/salidaE1.html', ctx)

def salidaTelas3(request, id, id_estante):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = request.POST.get('numeroRollo')
        cantidadYarda = request.POST.get('cantidad')
        
        idEst = Estante.objects.get(pk=3)
        ds = DetalleSalida(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, cantidadYarda=cantidadYarda, estante=idEst)
        ds.save()

    dicti ={'t': id, 'e': id_estante}
    it = get_object_or_404(Inventario, tela=dicti.get('t'))
    t = Tela.objects.get(pk=dicti.get('t'))
    if request.method == 'POST':
        add_stock = int(request.POST.get('cantidad'))

        if it.cantidadYarda  >= 1 and  add_stock <= it.cantidadYarda:
            it.cantidadYarda -= add_stock
            it.save()
            
        else:
            msj = 'Cantidad insuficiente en stock'
            messages.add_message(request,messages.INFO, msj)
            
        telas = Tela.objects.all().order_by('nombre')
        inv = Inventario.objects.filter(estante=3)
        ctx ={
                'inv' : inv,
                'telas': telas,
                'msj':'success',
            }
        return render(request, 'inventario/Estante3/salidaE1.html', ctx)
    
    data = Tela.objects.all().order_by('nombre')
    inv = Inventario.objects.filter(estante=3)
    ctx = {
        'telas': data,
        't': t,
        'inv' : inv,
        'it' : it,
    }
    return render(request, 'inventario/Estante3/salidaE1.html', ctx)

def entradaE3(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = int(request.POST.get('numeroRollo'))
        cantidadYarda = int(request.POST.get('cantidadYarda'))
        IdTela = int(request.POST.get('tipoTela'))
        tipoTela = Tipo_Tela.objects.get(pk=IdTela)
        
        try:
            tela = Tela.objects.get(nombre=nombre)
        except:
            pass
        
        variable = ''
        try:
            variable = Inventario.objects.get(tela=tela)
            
        except:
            pass

        if Tela.objects.filter(nombre=nombre) and variable != '':

            data = Tela.objects.all().order_by('nombre')
            inventario = Inventario.objects.all()
            ctx = {
                'tela': data,
                'msj':'danger',
                'inventario' : inventario
            }
            msj = 'La tela ya existe!'
            messages.add_message(request,messages.INFO, msj)
            return render(request, 'inventario/entradaE1.html', ctx)

        try:
            telas
        except:
            p = Tela(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, tipoTela=tipoTela)
            p.save()
            
        telasInv = Tela.objects.get(nombre=nombre)
        idEst = Estante.objects.get(pk=3)
        inv = Inventario(estante=idEst,tela=telasInv, cantidadYarda=cantidadYarda)
        inv.save()

        msj = 'Tela registrada correctamente.'
        messages.add_message(request, messages.INFO, msj)
        
        data = Tela.objects.all().order_by('nombre')
        inventario = Inventario.objects.all()
        ctx = {
            'telas': data,
            'tipoTela': Tipo_Tela.objects.all(),
            'msj':'success',
            'inventario' : inventario
        }
        
        return render(request, 'inventario/Estante3/entradaE1.html', ctx)

    telas = Tela.objects.all().order_by('nombre')
    inventario = Inventario.objects.all()

    ctx ={
        'telas': telas,
        'tipoTela': Tipo_Tela.objects.all(),
        'inventario': inventario,
    }
    return render(request, 'inventario/Estante3/entradaE1.html', ctx)

#ESTANTE 4
def inventarioE4(request):
    inventarioTela = Inventario.objects.filter(estante=4)
    tela = Tela.objects.all()
    
    ctx = {
        'inventarioTela': inventarioTela,
        'tela': tela,
    }

    return render(request, 'inventario/Estante4/inventarioE1.html',ctx)

def salidaE4(request):
    inventario = Inventario.objects.filter(estante=4,cantidadYarda__gt = 0)
    tela = Tela.objects.all()
    ctx ={
        'tela': tela,
        'inv' : inventario,
    }
    return render(request, 'inventario/Estante4/salidaE1.html', ctx)

def salidaTelas4(request, id, id_estante):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = request.POST.get('numeroRollo')
        cantidadYarda = request.POST.get('cantidad')
        
        idEst = Estante.objects.get(pk=4)
        ds = DetalleSalida(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, cantidadYarda=cantidadYarda, estante=idEst)
        ds.save()

    dicti ={'t': id, 'e': id_estante}
    it = get_object_or_404(Inventario, tela=dicti.get('t'))
    t = Tela.objects.get(pk=dicti.get('t'))
    if request.method == 'POST':
        add_stock = int(request.POST.get('cantidad'))

        if it.cantidadYarda  >= 1 and  add_stock <= it.cantidadYarda:
            it.cantidadYarda -= add_stock
            it.save()
            
        else:
            msj = 'Cantidad insuficiente en stock'
            messages.add_message(request,messages.INFO, msj)
            
        telas = Tela.objects.all().order_by('nombre')
        inv = Inventario.objects.filter(estante=4)
        ctx ={
                'inv' : inv,
                'telas': telas,
                'msj':'success',
            }
        return render(request, 'inventario/Estante4/salidaE1.html', ctx)
    
    data = Tela.objects.all().order_by('nombre')
    inv = Inventario.objects.filter(estante=4)
    ctx = {
        'telas': data,
        't': t,
        'inv' : inv,
        'it' : it,
    }
    return render(request, 'inventario/Estante4/salidaE1.html', ctx)

def entradaE4(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = int(request.POST.get('numeroRollo'))
        cantidadYarda = int(request.POST.get('cantidadYarda'))
        IdTela = int(request.POST.get('tipoTela'))
        tipoTela = Tipo_Tela.objects.get(pk=IdTela)
        
        try:
            tela = Tela.objects.get(nombre=nombre)
        except:
            pass
        
        variable = ''
        try:
            variable = Inventario.objects.get(tela=tela)
            
        except:
            pass

        if Tela.objects.filter(nombre=nombre) and variable != '':

            data = Tela.objects.all().order_by('nombre')
            inventario = Inventario.objects.all()
            ctx = {
                'tela': data,
                'msj':'danger',
                'inventario' : inventario
            }
            msj = 'La tela ya existe!'
            messages.add_message(request,messages.INFO, msj)
            return render(request, 'inventario/Estante4/entradaE1.html', ctx)

        try:
            telas
        except:
            p = Tela(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, tipoTela=tipoTela)
            p.save()
            
        telasInv = Tela.objects.get(nombre=nombre)
        idEst = Estante.objects.get(pk=4)
        inv = Inventario(estante=idEst,tela=telasInv, cantidadYarda=cantidadYarda)
        inv.save()

        msj = 'Tela registrada correctamente.'
        messages.add_message(request, messages.INFO, msj)
        
        data = Tela.objects.all().order_by('nombre')
        inventario = Inventario.objects.all()
        ctx = {
            'telas': data,
            'tipoTela': Tipo_Tela.objects.all(),
            'msj':'success',
            'inventario' : inventario
        }
        
        return render(request, 'inventario/Estante4/entradaE1.html', ctx)

    telas = Tela.objects.all().order_by('nombre')
    inventario = Inventario.objects.all()

    ctx ={
        'telas': telas,
        'tipoTela': Tipo_Tela.objects.all(),
        'inventario': inventario,
    }
    return render(request, 'inventario/Estante4/entradaE1.html', ctx)

#ESTANTE 5
def inventarioE5(request):
    inventarioTela = Inventario.objects.filter(estante=5)
    tela = Tela.objects.all()
    
    ctx = {
        'inventarioTela': inventarioTela,
        'tela': tela,
    }

    return render(request, 'inventario/Estante5/inventarioE1.html',ctx)

def salidaE5(request):
    inventario = Inventario.objects.filter(estante=5)
    tela = Tela.objects.all()
    ctx ={
        'tela': tela,
        'inv' : inventario,
    }
    return render(request, 'inventario/Estante5/salidaE1.html', ctx)

def salidaTelas5(request, id, id_estante):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = request.POST.get('numeroRollo')
        cantidadYarda = request.POST.get('cantidad')
        
        idEst = Estante.objects.get(pk=5)
        ds = DetalleSalida(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, cantidadYarda=cantidadYarda, estante=idEst)
        ds.save()

    dicti ={'t': id, 'e': id_estante}
    it = get_object_or_404(Inventario, tela=dicti.get('t'))
    t = Tela.objects.get(pk=dicti.get('t'))
    if request.method == 'POST':
        add_stock = int(request.POST.get('cantidad'))

        if it.cantidadYarda  >= 1 and  add_stock <= it.cantidadYarda:
            it.cantidadYarda -= add_stock
            it.save()
            
        else:
            msj = 'Cantidad insuficiente en stock'
            messages.add_message(request,messages.INFO, msj)
            
        telas = Tela.objects.all().order_by('nombre')
        inv = Inventario.objects.filter(estante=5)
        ctx ={
                'inv' : inv,
                'telas': telas,
                'msj':'success',
            }
        return render(request, 'inventario/Estante5/salidaE1.html', ctx)
    
    data = Tela.objects.all().order_by('nombre')
    inv = Inventario.objects.filter(estante=5)
    ctx = {
        'telas': data,
        't': t,
        'inv' : inv,
        'it' : it,
    }
    return render(request, 'inventario/Estante5/salidaE1.html', ctx)

def entradaE5(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = int(request.POST.get('numeroRollo'))
        cantidadYarda = int(request.POST.get('cantidadYarda'))
        IdTela = int(request.POST.get('tipoTela'))
        tipoTela = Tipo_Tela.objects.get(pk=IdTela)
        
        try:
            tela = Tela.objects.get(nombre=nombre)
        except:
            pass
        
        variable = ''
        try:
            variable = Inventario.objects.get(tela=tela)
            
        except:
            pass

        if Tela.objects.filter(nombre=nombre) and variable != '':

            data = Tela.objects.all().order_by('nombre')
            inventario = Inventario.objects.all()
            ctx = {
                'tela': data,
                'msj':'danger',
                'inventario' : inventario
            }
            msj = 'La tela ya existe!'
            messages.add_message(request,messages.INFO, msj)
            return render(request, 'inventario/Estante5/entradaE1.html', ctx)

        try:
            telas
        except:
            p = Tela(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, tipoTela=tipoTela)
            p.save()
            
        telasInv = Tela.objects.get(nombre=nombre)
        idEst = Estante.objects.get(pk=5)
        inv = Inventario(estante=idEst,tela=telasInv, cantidadYarda=cantidadYarda)
        inv.save()

        msj = 'Tela registrada correctamente.'
        messages.add_message(request, messages.INFO, msj)
        
        data = Tela.objects.all().order_by('nombre')
        inventario = Inventario.objects.all()
        ctx = {
            'telas': data,
            'tipoTela': Tipo_Tela.objects.all(),
            'msj':'success',
            'inventario' : inventario
        }
        
        return render(request, 'inventario/Estante5/entradaE1.html', ctx)

    telas = Tela.objects.all().order_by('nombre')
    inventario = Inventario.objects.all()

    ctx ={
        'telas': telas,
        'tipoTela': Tipo_Tela.objects.all(),
        'inventario': inventario,
    }
    return render(request, 'inventario/Estante5/entradaE1.html', ctx)

#ESTANTE 6
def inventarioE6(request):
    inventarioTela = Inventario.objects.filter(estante=6)
    tela = Tela.objects.all()
    
    ctx = {
        'inventarioTela': inventarioTela,
        'tela': tela,
    }

    return render(request, 'inventario/Estante6/inventarioE1.html',ctx)

def salidaE6(request):
    inventario = Inventario.objects.filter(estante=6)
    tela = Tela.objects.all()
    ctx ={
        'tela': tela,
        'inv' : inventario,
    }
    return render(request, 'inventario/Estante6/salidaE1.html', ctx)

def salidaTelas6(request, id, id_estante):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = request.POST.get('numeroRollo')
        cantidadYarda = request.POST.get('cantidad')
        
        idEst = Estante.objects.get(pk=6)
        ds = DetalleSalida(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, cantidadYarda=cantidadYarda, estante=idEst)
        ds.save()

    dicti ={'t': id, 'e': id_estante}
    it = get_object_or_404(Inventario, tela=dicti.get('t'))
    t = Tela.objects.get(pk=dicti.get('t'))
    if request.method == 'POST':
        add_stock = int(request.POST.get('cantidad'))

        if it.cantidadYarda  >= 1 and  add_stock <= it.cantidadYarda:
            it.cantidadYarda -= add_stock
            it.save()
            
        else:
            msj = 'Cantidad insuficiente en stock'
            messages.add_message(request,messages.INFO, msj)
            
        telas = Tela.objects.all().order_by('nombre')
        inv = Inventario.objects.filter(estante=6)
        ctx ={
                'inv' : inv,
                'telas': telas,
                'msj':'success',
            }
        return render(request, 'inventario/Estante6/salidaE1.html', ctx)
    
    data = Tela.objects.all().order_by('nombre')
    inv = Inventario.objects.filter(estante=6)
    ctx = {
        'telas': data,
        't': t,
        'inv' : inv,
        'it' : it,
    }
    return render(request, 'inventario/Estante6/salidaE1.html', ctx)

def entradaE6(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calidad = request.POST.get('calidad')
        color = request.POST.get('color')
        numeroRollo = int(request.POST.get('numeroRollo'))
        cantidadYarda = int(request.POST.get('cantidadYarda'))
        IdTela = int(request.POST.get('tipoTela'))
        tipoTela = Tipo_Tela.objects.get(pk=IdTela)
        
        try:
            tela = Tela.objects.get(nombre=nombre)
        except:
            pass
        
        variable = ''
        try:
            variable = Inventario.objects.get(tela=tela)
            
        except:
            pass

        if Tela.objects.filter(nombre=nombre) and variable != '':

            data = Tela.objects.all().order_by('nombre')
            inventario = Inventario.objects.all()
            ctx = {
                'tela': data,
                'msj':'danger',
                'inventario' : inventario
            }
            msj = 'La tela ya existe!'
            messages.add_message(request,messages.INFO, msj)
            return render(request, 'inventario/Estante1/entradaE1.html', ctx)

        try:
            telas
        except:
            p = Tela(nombre=nombre, calidad=calidad, color=color, numeroRollo=numeroRollo, tipoTela=tipoTela)
            p.save()
            
        telasInv = Tela.objects.get(nombre=nombre)
        idEst = Estante.objects.get(pk=6)
        inv = Inventario(estante=idEst,tela=telasInv, cantidadYarda=cantidadYarda)
        inv.save()

        msj = 'Tela registrada correctamente.'
        messages.add_message(request, messages.INFO, msj)
        
        data = Tela.objects.all().order_by('nombre')
        inventario = Inventario.objects.all()
        ctx = {
            'telas': data,
            'tipoTela': Tipo_Tela.objects.all(),
            'msj':'success',
            'inventario' : inventario
        }
        
        return render(request, 'inventario/Estante6/entradaE1.html', ctx)

    telas = Tela.objects.all().order_by('nombre')
    inventario = Inventario.objects.all()

    ctx ={
        'telas': telas,
        'tipoTela': Tipo_Tela.objects.all(),
        'inventario': inventario,
    }
    return render(request, 'inventario/Estante6/entradaE1.html', ctx)
