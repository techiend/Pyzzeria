from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Pedido

def index(request):
    return HttpResponse("Solicitar pedido")

def lista(request):
    pedidos_list = Pedido.objects.order_by('-fecha_pedido')[0:]
    context = {'pedidos_list': pedidos_list, }
    return render(request, 'pedidos/lista.html', context)

def detail(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'pedidos/detail.html', {'pedido': pedido})