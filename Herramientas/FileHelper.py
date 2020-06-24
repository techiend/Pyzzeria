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
            print(f"Archivo {pedidoPath} procesado.")
    else:
        print(f"ERRROR \n¡¡ El archivo {pedidoPath} no existe !!")

# se crea el archivo resumen
def write_file(filepath="resumen.pz"):
 # se toman los datos de la base de datos 
    cur = CONNECTION.cursor()
    subtotal_tamano = cur.execute(f'''select distinct  p.fecha_pedido,(select sum(t.costo_tamano) from tamano t, pizza pi, pedido pe where pi.fk_tamano=t.id and pe.fecha_pedido =p.fecha_pedido  and pi.fk_pedido=pe.id )
                                      from pedido p, pizza pi, tamano t 
                                      where  p.id= pi.fk_pedido and  t.id= pi.fk_tamano''').fetchall()
    
    subtotal_ingre = cur.execute(f'''  select distinct p.fecha_pedido, 
                                  (select sum(t_ing.precio_ingrediente)
                                   from pedido pe, pizza piz, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_ing, ingrediente i  
                                   where pe.id= piz.fk_pedido and  t.id= piz.fk_tamano and t_ing.fk_ingrediente= i.id and 
                                      t_ing.fk_tamano = t.id and piz.id= pi_in.fk_id_pizza and piz.fk_tamano= pi_in.fk_tamano_pizza 
                                      and pi_in.fk_ti_ingrediente=t_ing.fk_ingrediente and pe.fecha_pedido =p.fecha_pedido)

                                    from pedido p, pizza pi, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_in, ingrediente i
                                    where  p.id= pi.fk_pedido and  t.id= pi.fk_tamano and t_in.fk_ingrediente= i.id and 
                                      t_in.fk_tamano = t.id and pi.id= pi_in.fk_id_pizza and pi.fk_tamano= pi_in.fk_tamano_pizza 
                                      and t_in.fk_ingrediente= pi_in.fk_ti_ingrediente and t_in.fk_tamano= pi_in.fk_ti_tamano_ingrediente''').fetchall()

    vent_piz= cur.execute(f'''select distinct  p.fecha_pedido, t.nombre_tamano,
(select count(*) from pizza pi, pedido pe where pi.fk_tamano=1 and pe.fecha_pedido =p.fecha_pedido  and pi.fk_pedido=pe.id),
(select count(*) from pizza pi, pedido pe where pi.fk_tamano=2 and pe.fecha_pedido =p.fecha_pedido  and pi.fk_pedido=pe.id),
(select count(*) from pizza pi, pedido pe where pi.fk_tamano=3 and pe.fecha_pedido =p.fecha_pedido  and pi.fk_pedido=pe.id),
(select sum(t.costo_tamano) from tamano t, pizza pi, pedido pe where pi.fk_tamano=1 and pi.fk_tamano=t.id  and pe.fecha_pedido =p.fecha_pedido  and pi.fk_pedido=pe.id ),
(select sum(t.costo_tamano) from tamano t, pizza pi, pedido pe where pi.fk_tamano=2 and pi.fk_tamano=t.id and pe.fecha_pedido =p.fecha_pedido  and pi.fk_pedido=pe.id ),
(select sum(t.costo_tamano) from tamano t, pizza pi, pedido pe where pi.fk_tamano=3 and pi.fk_tamano=t.id and pe.fecha_pedido =p.fecha_pedido  and pi.fk_pedido=pe.id )
from pedido p, pizza pi, tamano t 
where  p.id= pi.fk_pedido and  t.id= pi.fk_tamano  ''').fetchall()
    
    vent_ing= cur.execute(f'''select distinct p.fecha_pedido,  i.nombre_ingrediente,
(select count(*) 
 from pizza_ingrediente pi_ing, pizza pi, pedido pe
 where pi_ing.fk_ti_ingrediente=1 and pe.fecha_pedido =p.fecha_pedido
 and pi.fk_pedido=pe.id and pi_ing.fk_id_pizza=pi.id),
(select count(*) from pizza_ingrediente pi_ing, pizza pi, pedido pe where pi_ing.fk_ti_ingrediente=2 and pe.fecha_pedido =p.fecha_pedido
 and pi.fk_pedido=pe.id and pi_ing.fk_id_pizza=pi.id),
(select count(*) from pizza_ingrediente pi_ing, pizza pi, pedido pe where pi_ing.fk_ti_ingrediente=3 and pe.fecha_pedido =p.fecha_pedido
 and pi.fk_pedido=pe.id and pi_ing.fk_id_pizza=pi.id),
(select count(*) from pizza_ingrediente pi_ing, pizza pi, pedido pe where pi_ing.fk_ti_ingrediente=4 and pe.fecha_pedido =p.fecha_pedido
 and pi.fk_pedido=pe.id and pi_ing.fk_id_pizza=pi.id),
(select count(*) from pizza_ingrediente pi_ing, pizza pi, pedido pe where pi_ing.fk_ti_ingrediente=5 and pe.fecha_pedido =p.fecha_pedido
 and pi.fk_pedido=pe.id and pi_ing.fk_id_pizza=pi.id),
(select count(*) from pizza_ingrediente pi_ing, pizza pi, pedido pe where pi_ing.fk_ti_ingrediente=6 and pe.fecha_pedido =p.fecha_pedido
 and pi.fk_pedido=pe.id and pi_ing.fk_id_pizza=pi.id),
(select count(*) from pizza_ingrediente pi_ing, pizza pi, pedido pe where pi_ing.fk_ti_ingrediente=7 and pe.fecha_pedido =p.fecha_pedido
 and pi.fk_pedido=pe.id and pi_ing.fk_id_pizza=pi.id),

(select sum(t_ing.precio_ingrediente)
from pedido pe, pizza piz, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_ing, ingrediente i  
where t_ing.fk_ingrediente= 1 and pe.id= piz.fk_pedido and  t.id= piz.fk_tamano and t_ing.fk_ingrediente= i.id and 
t_ing.fk_tamano = t.id and piz.id= pi_in.fk_id_pizza and piz.fk_tamano= pi_in.fk_tamano_pizza 
and pi_in.fk_ti_ingrediente=t_ing.fk_ingrediente and pe.fecha_pedido =p.fecha_pedido),

(select sum(t_ing.precio_ingrediente)
from pedido pe, pizza piz, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_ing, ingrediente i  
where t_ing.fk_ingrediente= 2 and pe.id= piz.fk_pedido and  t.id= piz.fk_tamano and t_ing.fk_ingrediente= i.id and 
t_ing.fk_tamano = t.id and piz.id= pi_in.fk_id_pizza and piz.fk_tamano= pi_in.fk_tamano_pizza 
and pi_in.fk_ti_ingrediente=t_ing.fk_ingrediente and pe.fecha_pedido =p.fecha_pedido),

(select sum(t_ing.precio_ingrediente)
from pedido pe, pizza piz, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_ing, ingrediente i  
where t_ing.fk_ingrediente= 3 and pe.id= piz.fk_pedido and  t.id= piz.fk_tamano and t_ing.fk_ingrediente= i.id and 
t_ing.fk_tamano = t.id and piz.id= pi_in.fk_id_pizza and piz.fk_tamano= pi_in.fk_tamano_pizza 
and pi_in.fk_ti_ingrediente=t_ing.fk_ingrediente and pe.fecha_pedido =p.fecha_pedido),

(select sum(t_ing.precio_ingrediente)
from pedido pe, pizza piz, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_ing, ingrediente i  
where t_ing.fk_ingrediente= 4 and pe.id= piz.fk_pedido and  t.id= piz.fk_tamano and t_ing.fk_ingrediente= i.id and 
t_ing.fk_tamano = t.id and piz.id= pi_in.fk_id_pizza and piz.fk_tamano= pi_in.fk_tamano_pizza 
and pi_in.fk_ti_ingrediente=t_ing.fk_ingrediente and pe.fecha_pedido =p.fecha_pedido),

(select sum(t_ing.precio_ingrediente)
from pedido pe, pizza piz, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_ing, ingrediente i  
where t_ing.fk_ingrediente= 5 and pe.id= piz.fk_pedido and  t.id= piz.fk_tamano and t_ing.fk_ingrediente= i.id and 
t_ing.fk_tamano = t.id and piz.id= pi_in.fk_id_pizza and piz.fk_tamano= pi_in.fk_tamano_pizza 
and pi_in.fk_ti_ingrediente=t_ing.fk_ingrediente and pe.fecha_pedido =p.fecha_pedido),

(select sum(t_ing.precio_ingrediente)
from pedido pe, pizza piz, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_ing, ingrediente i  
where t_ing.fk_ingrediente= 6 and pe.id= piz.fk_pedido and  t.id= piz.fk_tamano and t_ing.fk_ingrediente= i.id and 
t_ing.fk_tamano = t.id and piz.id= pi_in.fk_id_pizza and piz.fk_tamano= pi_in.fk_tamano_pizza 
and pi_in.fk_ti_ingrediente=t_ing.fk_ingrediente and pe.fecha_pedido =p.fecha_pedido),

(select sum(t_ing.precio_ingrediente)
from pedido pe, pizza piz, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_ing, ingrediente i  
where t_ing.fk_ingrediente= 7 and pe.id= piz.fk_pedido and  t.id= piz.fk_tamano and t_ing.fk_ingrediente= i.id and 
t_ing.fk_tamano = t.id and piz.id= pi_in.fk_id_pizza and piz.fk_tamano= pi_in.fk_tamano_pizza 
and pi_in.fk_ti_ingrediente=t_ing.fk_ingrediente and pe.fecha_pedido =p.fecha_pedido)

from pedido p, pizza pi, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_in, ingrediente i
where  p.id= pi.fk_pedido and  t.id= pi.fk_tamano and t_in.fk_ingrediente= i.id and 
t_in.fk_tamano = t.id and pi.id= pi_in.fk_id_pizza and pi.fk_tamano= pi_in.fk_tamano_pizza 
and t_in.fk_ingrediente= pi_in.fk_ti_ingrediente and t_in.fk_tamano= pi_in.fk_ti_tamano_ingrediente ''').fetchall()