import os
from .DBHelper import CONNECTION, addPedido, addPizza, subt_tam, subt_ing, vnt_piz, vnt_ing

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
            print(f"Archivo {pedidoPath} procesado.")
    else:
        print(f"ERRROR \n¡¡ El archivo {pedidoPath} no existe !!")

# funcion para crear el archivo resumen
def write_file(filepath="resumen.pz"):
    #llamar a las funciones de los querys para obtener los datos
    subt_tm=subt_tam() #total de las ventas de los tamaños
    subt_ig=subt_ing() #total de las ventas de los ingredientes
    vt_pz=vnt_piz() #venta por tamaño con sus respectivas unidades y montos
    vt_ig=vnt_ing() #venta por ingrediente con sus respectivas unidades y montos
      
    dic_venta_t={}
    #se recorre los dos arreglos para crear el diccionario de fechas y montos totales
    #sumar sub totales para hallar venta total 
    #x y representan los elementos de cada arreglo
    for x in subt_tm:
        if x[0] in dic_venta_t.keys():
            dic_venta_t[x[0]]=dic_venta_t[x[0]]+float(x[1])
        else:
          dic_venta_t[x[0]]=x[1]  

    for y in subt_ig:
        if y[0] in dic_venta_t.keys():
            dic_venta_t[y[0]]=dic_venta_t[y[0]]+float(y[1])
        else:
          dic_venta_t[y[0]]=y[1]    
    
    #creacion y llenado del archivo
    resumen = open("resumen.pz","w")
    #ciclo que por cada llave (a) del diccionario se escribe en el archivo resumen
    for a in dic_venta_t:
            resumen.write('\n'+'\n')
            resumen.write("Fecha: "+a +'\n')
            resumen.write("Venta Total: "+ str (dic_venta_t[a])+" UMs"+'\n')
            resumen.write("Ventas por pizza (sin incluir adicionales): "+'\n')
            resumen.write('\t'+"Pizza  "+'\t'+'\t'+'\t'+'\t'+"||"+"Unidades"+'\t'+'\t'+"||"+"Mono UMs"+'\n')
            
            """ciclo que por cada elemento(b) de venta tamaño se escribe en
             el archivo los tamaños que se vendieron ese dia junto con sus cantidades y montos"""
            for b in vt_pz:
               if a==b[0]:
                   # se escribe en el archivo los tamaños, unidades y montos
                   if str(b[1])=='mediana':
                       medi=str(b[1])+' '
                       resumen.write('\t'+medi.capitalize()+'\t'+'\t'+'\t'+"||"+str(b[2])+'\t'+'\t'+'\t'+'\t'+"||"+str(b[3])+'\n')
                   else:
                       
                       resumen.write('\t'+str(b[1]).capitalize()+'\t'+'\t'+'\t'+"||"+str(b[2])+'\t'+'\t'+'\t'+'\t'+"||"+str(b[3])+'\n')

            resumen.write("Ventas por Ingrediente: "+'\n')
            resumen.write('\t'+"Ingredientes  "+'\t'+'\t'+"||"+"Unidades"+'\t'+'\t'+"||"+"Mono UMs"+'\n') 

            """ciclo que por cada elemento(c) de venta ingrediente se escribe en
            el archivo los ingredientes que se vendieron ese dia junto con sus cantidades y montos"""
            for c in vt_ig:
               if a==c[0]: 
                   # se escribe en el archivo los ingredientes, unidades y montos
                    if str(c[1])=='jamon':
                           jamon=str(c[1])+'   '
                           resumen.write('\t'+jamon.capitalize()+'\t'+'\t'+'\t'+"||"+str(c[2])+'\t'+'\t'+'\t'+'\t'+"||"+str(c[3])+'\n')
                    else:
                           
                           resumen.write('\t'+str(c[1]).capitalize()+'\t'+'\t'+'\t'+"||"+str(c[2])+'\t'+'\t'+'\t'+'\t'+"||"+str(c[3])+'\n')      

    resumen.close() 

