from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone 
from .models import Pedido, Tamano, Ingrediente

def index(request):
    return render(request, 'pedidos/index.html')

def lista(request):
    pedidos_list = Pedido.objects.order_by('-fecha_pedido')[0:]
    context = {'pedidos_list': pedidos_list, }
    return render(request, 'pedidos/lista.html', context)

def detail(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'pedidos/detail.html', {'pedido': pedido})

def solicitud(request):
    try:
        name = request.POST['name']
        if name == "":
            return render(request, 'pedidos/index.html', {
                'error_message': "Error, nombre no puede estar vacio.",
            })
    except:
        return render(request, 'pedidos/index.html', {
            'error_message': "Error, no existe el campo name.",
        })
    else:
        pedido = Pedido(fecha_pedido=timezone.now(),nombre_cliente=name)
        pedido.save()
        return render(request, 'pedidos/tamano.html', {
            'pedido_id': pedido.pedido_id,
            'tamano': Tamano.objects.all(),
            'ing': Ingrediente.objects.all(),
        })
