from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone 
from .models import Pedido, Tamano, Ingrediente, Pizza, Pizza_Ingrediente

def index(request):
    return render(request, 'pedidos/index.html')

def lista(request):
    pedidos_list = Pedido.objects.order_by('-fecha_pedido')[0:]
    context = {'pedidos_list': pedidos_list, }
    return render(request, 'pedidos/lista.html', context)

def detail(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'pedidos/detail.html', {'pedido': pedido})

def admin(request):
    # pedidos_list = Pedido.objects.order_by('fecha_pedido')[0:]
    pedidos = list()
    pedidos_list = Pedido.objects.order_by('fecha_pedido')[0:]
    for pl in pedidos_list:
        pizzas = pl.pizza_set.all()
        if pizzas:
            pedidos.append(pl)
    return render(request, 'pedidos/administracion.html', {'pedidos_list': pedidos})

def admin_detalle(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'pedidos/adetalle.html', {'pedido': pedido})

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

def pizza(request):
    try:
        pedidoID = request.POST['pedidoID']
        selTamano = '-1'
        if 'selTamano' in request.POST:
            selTamano = request.POST['selTamano']
        else:
            return render(request, 'pedidos/tamano.html', {
                'pedido_id': pedidoID,
                'tamano': Tamano.objects.all(),
                'ing': Ingrediente.objects.all(),
                'error_message': "Error, debes seleccionar un tamaño",
            })

        ingredients = list()
        if 'ingredients' in request.POST:
            ingredients = request.POST.getlist('ingredients')

        boton = request.POST['action']

        if pedidoID == "":
            return render(request, 'pedidos/index.html', {
                'error_message': "Error, vuelve a intentarlo.",
            })

        print("ID= "+str(pedidoID))
        print("Tamano= "+str(selTamano))
        print("Ingrediente= "+str(ingredients))
        print("Boton= "+str(boton))

        pedido = Pedido.objects.get(pedido_id=pedidoID)
        tamano = Tamano.objects.get(tamano_id=selTamano)

        pizza = pedido.pizza_set.create(pedido_id=pedido,tamano_id=tamano)
        # pizza.save()

        print("Pizza ID= "+ str(pizza.pizza_id))
        for ingr in ingredients:
            print("algo: " + str(ingr))
            i = Ingrediente.objects.get(ingrediente_id=ingr)
            pizza_ing = pizza.pizza_ingrediente_set.create(pizza_id=pizza,ingrediente_id=i)
            # pizza_ing.save()

        if boton == "add":
            return render(request, 'pedidos/tamano.html', {
                'pedido_id': pedidoID,
                'tamano': Tamano.objects.all(),
                'ing': Ingrediente.objects.all(),
            })
            
        if boton == "end":
            # return redirect(detail, pedido_id=pedidoID)
            return render(request, 'pedidos/detail.html', {
                'pedido': pedido,
                # 'tamano': Tamano.objects.all(),
                # 'ing': Ingrediente.objects.all(),
                # 'error_message': "Pedido completo.",
            })

    except:
        if pedidoID != "":
            return render(request, 'pedidos/index.html', {
                'error_message': "Error, vuelve a intentarlo.",
            })
    else:
        return render(request, 'pedidos/tamano.html', {
            'pedido_id': pedidoID,
            'tamano': Tamano.objects.all(),
            'ing': Ingrediente.objects.all(),
        })


#
def venta_ingrediente(request):

   
    raw_query = '''
                select pedidos_pedido.pedido_id, 
                pedidos_ingrediente.nombre_ingrediente, 
                count(pedidos_ingrediente.ingrediente_id) Cantidad,
                count(pedidos_ingrediente.ingrediente_id) * pedidos_ingrediente.costo_ingrediente Monto
                from pedidos_ingrediente , pedidos_pedido , pedidos_pizza ,pedidos_pizza_ingrediente 
                where pedidos_pizza.pedido_id_id = pedidos_pedido.pedido_id and
                 pedidos_pizza_ingrediente.pizza_id_id = pedidos_pizza.pizza_id 
                 and pedidos_pizza_ingrediente.ingrediente_id_id = pedidos_ingrediente.ingrediente_id
                group by pedidos_ingrediente.nombre_ingrediente
        '''
    
    results = Pedido.objects.raw(raw_query)
    return render(request, 'pedidos/venta_ingrediente.html', {'resultado': results})

def venta_tamano(request):

   
    raw_query = '''
                select pedidos_pedido.pedido_id, 
                pedidos_tamano.nombre_tamano, 
                count(pedidos_pizza.tamano_id_id) Cantidad,
                count(pedidos_pizza.tamano_id_id) * pedidos_tamano.costo_tamano Monto
                from  pedidos_pedido , pedidos_pizza, pedidos_tamano 
                where pedidos_pizza.pedido_id_id = pedidos_pedido.pedido_id and
                pedidos_pizza.tamano_id_id = pedidos_tamano.tamano_id
                group by pedidos_tamano.nombre_tamano
        '''
    
    results = Pedido.objects.raw(raw_query)
    return render(request, 'pedidos/venta_tamano.html', {'resultado': results})



    
    