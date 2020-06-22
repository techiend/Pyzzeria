import os
from .DBHelper import CONNECTION, addPedido, addPizza

def read_file(filepath="pedidos1.pz"):
    # Para leer los archivos
    t = os.path.isfile(filepath)
    if (t == True):
        f = open(filepath, "r")   
        # if f.mode == "r":
        #     contenido = f.read()
        #     print(contenido)
        f1 = f.readlines()
        for x in f1:
            print(x)
        f.close()
    else:
        print("ERRROR \n¡¡ El archivo no existe !!")
    return

def fixLine(line):
    line = line.lower()
    line = line.replace('\n','')
    line = line.replace('á','a')
    line = line.replace('é','e')
    line = line.replace('í','i')
    line = line.replace('ó','o')
    line = line.replace('ú','u')
    line = line.replace('ñ','n')
    return line

def procesar(pedidoPath='pedidos1.pz'):
    ''' Para procesar el archivo de los pedidos '''
    idPedido = 0
    line = 0
    t = os.path.isfile(pedidoPath)
    if t == True:
        with open(pedidoPath, mode="r", encoding="utf-8") as f:
            f1 = f.readlines()
            for x in f1:
                x = fixLine(x)
                # if x.startswith("COMIENZO_PEDIDO") or x.startswith("FIN_PEDIDO"):
                if x.startswith("comienzo_pedido") or x.startswith("fin_pedido"):
                    ''' Reiniciar los contadores al comienzo del pedido '''
                    line = 1
                elif line == 1:
                    ''' La primera linea es nuestra informacion del cliente y la fecha del pedido '''
                    separa = x.split(";")
                    nombre = separa[0].strip()
                    fecha = separa[1].strip()
                    if nombre == '' or fecha == '':
                        print('"Nombre" y "Fecha" son los parametros requeridos para crear el Pedido.')
                        idPedido = 0
                        line = 0
                    else:
                        idPedido = addPedido(nombre, fecha)
                        # idPedido += 1
                        line += 1
                elif line > 1:
                    if idPedido != 0:
                        # print(f"Pedido #{idPedido}")
                        pizza = x.split(";")
                        tamano = pizza[0].strip()
                        # print("Tamano: ", tamano)
                        # print("Ingredientes: ", str(pizza[1:]))
                        addPizza(idPedido,tamano,pizza[1:])
                        line += 1
    else:
        print(f"ERRROR \n¡¡ El archivo {pedidoPath} no existe !!")