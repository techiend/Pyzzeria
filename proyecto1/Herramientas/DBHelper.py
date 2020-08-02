import  sqlite3
import sqlite3 as lite
from sqlite3 import Error

''' Metodo para crear una conexion con la BD '''
def create_connection(database_name="pyzzeria.sql"):
    #  Crear coneccion de la bd que se aloja en memoria
    conn = None
    try: 
        # conn = sqlite3.connect(":memory:")
        conn = sqlite3.connect(database_name)
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()
    print("Conexion establecida")
    return conn

''' Metodo para crear las tablas de la BD , insertar los Tamaños de pizza
    con sus respectivos precios, insertar los Ingredientes e insertar los 
    Tamaño_Ingrediente el cual posee el precio por ingrediete '''
def create_tables():
    c1 = CONNECTION.cursor()
    # Tabla Pedido
    c1.execute('''CREATE TABLE IF NOT EXISTS pedido (id INT PRIMARY KEY NOT NULL,
                                        fecha_pedido TEXT NOT NULL,
                                        nombrecliente_pedido TEXT NOT NULL)''')
    # Tabla Tamaño
    c1.execute('''CREATE TABLE IF NOT EXISTS tamano (id INT PRIMARY KEY NOT NULL,
                                        nombre_tamano TEXT NOT NULL,
                                        costo_tamano REAL NOT NULL)''')
    # Tabla Ingrediente
    c1.execute('''CREATE TABLE IF NOT EXISTS ingrediente (id INT PRIMARY KEY NOT NULL,
                                            nombre_ingrediente TEXT NOT NULL)''')
    # Tabla Pizza
    c1.execute('''CREATE TABLE IF NOT EXISTS pizza (id INT NOT NULL,
                                        fk_pedido INT NOT NULL,
                                        fk_tamano INT NOT NULL,
                                        PRIMARY KEY (id, fk_tamano),
                                        FOREIGN KEY (fk_pedido) REFERENCES pedido (id),
                                        FOREIGN KEY (fk_tamano) REFERENCES tamano (id))''')
    # Tabla Tamaño_Ingrediente
    c1.execute('''CREATE TABLE IF NOT EXISTS tamano_ingrediente (
                                                                precio_ingrediente REAL NOT NULL,
                                                                fk_ingrediente INT NOT NULL,
                                                                fk_tamano INT NOT NULL,
                                                                
                                                                FOREIGN KEY (fk_ingrediente) REFERENCES ingrediente(id),
                                                                FOREIGN KEY (fk_tamano) REFERENCES tamano(id))''')
    # Tabla Pizza_Ingrediente
    c1.execute('''CREATE TABLE IF NOT EXISTS pizza_ingrediente (
                                                    fk_id_pizza INT NOT NULL,
                                                    fk_tamano_pizza INT NOT NULL,
                                                    fk_ti_tamano_ingrediente INT NOT NULL,
                                                    fk_ti_ingrediente INT NOT NULL,
                                                    FOREIGN KEY (fk_id_pizza, fk_tamano_pizza) REFERENCES pizza(id, fk_tamano),
                                                    FOREIGN KEY (fk_ti_ingrediente,fk_ti_tamano_ingrediente) REFERENCES tamano_ingrediente(fk_ingrediente, fk_tamano))''')
    
    # Insert de Tamaño
    idT = c1.execute('''SELECT MAX(id) FROM tamano''').fetchone()
    if idT[0] == None:
            c1.execute('''INSERT INTO tamano (id, nombre_tamano, costo_tamano) VALUES (1, 'personal', 10)''')
            c1.execute('''INSERT INTO tamano (id, nombre_tamano, costo_tamano) VALUES (2, 'mediana', 20)''')
            c1.execute('''INSERT INTO tamano (id, nombre_tamano, costo_tamano) VALUES (3, 'familiar', 30)''')
            print("Rows (tamano) added successfully")
            CONNECTION.commit()
    else:
        print("- Skip the inserts (tamano) -")

    # Insert de Ingrediente
    idI = c1.execute('''SELECT MAX(id) FROM ingrediente''').fetchone()
    if idI[0] == None:
        c1.execute('''INSERT INTO ingrediente (id, nombre_ingrediente) VALUES (1, 'jamon')''')
        c1.execute('''INSERT INTO ingrediente (id, nombre_ingrediente) VALUES (2, 'champinones')''')
        c1.execute('''INSERT INTO ingrediente (id, nombre_ingrediente) VALUES (3, 'pimenton')''')
        c1.execute('''INSERT INTO ingrediente (id, nombre_ingrediente) VALUES (4, 'doble queso')''')
        c1.execute('''INSERT INTO ingrediente (id, nombre_ingrediente) VALUES (5, 'aceitunas')''')
        c1.execute('''INSERT INTO ingrediente (id, nombre_ingrediente) VALUES (6, 'pepperoni')''')
        c1.execute('''INSERT INTO ingrediente (id, nombre_ingrediente) VALUES (7, 'salchichon')''')
        print("Rows (ingrediente) added successfully")
        CONNECTION.commit()
    else:
        print("- Skip the inserts (ingrediente) -")

    # Insert de Tamaño_Ingrediente
    idTI = c1.execute('''SELECT MAX(precio_ingrediente) FROM tamano_ingrediente''').fetchone()
    if idTI[0] == None:
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (1, 1, 1.50)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (1, 2, 1.75)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (1, 3, 2.00)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (2, 1, 1.75)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (2, 2, 2.05)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (2, 3, 2.50)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (3, 1, 1.50)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (3, 2, 1.75)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (3, 3, 2.00)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (4, 1, 0.80)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (4, 2, 1.30)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (4, 3, 1.70)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (5, 1, 1.80)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (5, 2, 2.15)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (5, 3, 2.60)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (6, 1, 1.25)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (6, 2, 1.70)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (6, 3, 1.90)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (7, 1, 1.60)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (7, 2, 1.85)''')
        c1.execute('''INSERT INTO tamano_ingrediente ( fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (7, 3, 2.10)''')
        print("Rows (tamano_ingrediente) added successfully")
        CONNECTION.commit()
    else:
        print("- Skip the inserts (tamano_ingrediente) -")

    c1.close()
    print("Tables created successfully")
    return

''' Metodo que verifica y retorna el *ULTIMO* ID de una tabla '''
def lastID(table):
    cur = CONNECTION.cursor()
    last = cur.execute(f"SELECT MAX(id) FROM {table}").fetchone()
    if last[0] == None:
        last = 1
    else:
        last = last[0] + 1
    return last

''' Metodo que inserta un Pedido '''
def addPedido(nombreCliente, fechaPedido):
    c1 = CONNECTION.cursor()
    idPedido = lastID("pedido")
    c1.execute('''INSERT INTO pedido (id, fecha_pedido, nombrecliente_pedido) 
                                        values (?, ?, ?)''',(idPedido, fechaPedido, nombreCliente))
    CONNECTION.commit() 
    print("Datos del Pedido insertado exitosamente")
    return idPedido

''' Metodo que inserta una Pizza '''
def addPizza(idPedido, tamano, ingredientes):
    cur = CONNECTION.cursor()
    idTamano = cur.execute(f'''SELECT id FROM tamano WHERE nombre_tamano = "{tamano}" ''').fetchone()
    idPizza = lastID("pizza")
    if idTamano == None:
        print("El tamaño ",tamano," no existe")
    else:
        cur.execute('''INSERT INTO pizza (id, fk_pedido, fk_tamano) VALUES (?, ?, ?)''',(idPizza, idPedido, idTamano[0]))
    
    for ing in ingredientes:
        idIngrediente = cur.execute(f'''SELECT id FROM ingrediente WHERE nombre_ingrediente = "{ing}" ''').fetchone()
        if idIngrediente == None:
            print("El ingrediente ",ing," no esta disponible\n")
            while True:
                print("¿ Desea su pizza sin",ing,"?\n")
                try:
                    option = str(input("Introduce una opcion (S/N): "))
                
                    if (option == "s" or option == "S"):
                        print("\n")
                        break
                    elif (option == "n" or option == "N"):
                        cur.execute(f'''DELETE FROM pizza_ingrediente WHERE fk_id_pizza = {idPizza} and fk_tamano_pizza = {idTamano[0]}''')
                        cur.execute(f'''DELETE FROM pizza WHERE id = {idPizza}''')
                        print("\nCancelada la pizza con",ing,"\n")
                        return
                except ValueError:
                    break
        else:
            cur.execute('''INSERT INTO pizza_ingrediente (fk_id_pizza, fk_tamano_pizza, fk_ti_tamano_ingrediente, fk_ti_ingrediente) 
                                        VALUES (?, ?, ?, ?)''',(idPizza, idTamano[0], idTamano[0], idIngrediente[0]))
    CONNECTION.commit() 
    print("¡ Pizza insertada exitosamente !")


CONNECTION = create_connection("pyzzeria.sql")
create_tables()

'''Funcion que retorna las ventas totales de los tamaños'''
def subt_tam():
    cur = CONNECTION.cursor()
    subtotal_tamano = cur.execute('''select distinct  p.fecha_pedido,(select sum(t.costo_tamano) from tamano t, pizza pi, pedido pe where pi.fk_tamano=t.id and pe.fecha_pedido =p.fecha_pedido  and pi.fk_pedido=pe.id )
                                      from pedido p, pizza pi, tamano t 
                                      where  p.id= pi.fk_pedido and  t.id= pi.fk_tamano''').fetchall()
    return subtotal_tamano

'''Funcion que retorna las ventas totales de los ingredientes'''
def subt_ing():
    cur = CONNECTION.cursor()    
    subtotal_ingre = cur.execute('''  select distinct p.fecha_pedido, 
                                  (select sum(t_ing.precio_ingrediente)
                                   from pedido pe, pizza piz, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_ing, ingrediente i  
                                   where pe.id= piz.fk_pedido and  t.id= piz.fk_tamano and t_ing.fk_ingrediente= i.id and 
                                      t_ing.fk_tamano = t.id and piz.id= pi_in.fk_id_pizza and piz.fk_tamano= pi_in.fk_tamano_pizza 
                                      and pi_in.fk_ti_ingrediente=t_ing.fk_ingrediente and pe.fecha_pedido =p.fecha_pedido)

                                    from pedido p, pizza pi, pizza_ingrediente pi_in, tamano t, tamano_ingrediente t_in, ingrediente i
                                    where  p.id= pi.fk_pedido and  t.id= pi.fk_tamano and t_in.fk_ingrediente= i.id and 
                                      t_in.fk_tamano = t.id and pi.id= pi_in.fk_id_pizza and pi.fk_tamano= pi_in.fk_tamano_pizza 
                                      and t_in.fk_ingrediente= pi_in.fk_ti_ingrediente and t_in.fk_tamano= pi_in.fk_ti_tamano_ingrediente''').fetchall()
    return subtotal_ingre

'''Funcion que retorna las ventas de  tamaños con sus cantidades y montos'''
def vnt_piz():
    cur = CONNECTION.cursor()  
    vent_piz= cur.execute('''select  p.fecha_pedido, t.nombre_tamano,count(p.id) as vendidos,
                                (count(pi.id) * t.costo_tamano) as ganancias
                                from pedido p, pizza pi, tamano t 
                                where  p.id= pi.fk_pedido and  t.id= pi.fk_tamano
                                group by p.fecha_pedido, t.nombre_tamano  ''').fetchall()
    return vent_piz

'''Funcion que retorna las ventas de los ingredientes con sus cantidades y montos'''
def vnt_ing():
    cur = CONNECTION.cursor()      
    vent_ing= cur.execute('''SELECT pedidos_ingredientes.fecha_pedido, pedidos_ingredientes.nombre_ingrediente,
                            sum(pedidos_ingredientes.vendidos) as vendidos,
                            sum(pedidos_ingredientes.ganancias) as ganancias from 
	                        (SELECT pedido.fecha_pedido, ingrediente.nombre_ingrediente, 
	                         count(ingrediente.nombre_ingrediente) vendidos,
	                         count(ingrediente.nombre_ingrediente) * tamano_ingrediente.precio_ingrediente ganancias
	                        from pedido, pizza, pizza_ingrediente, tamano_ingrediente, ingrediente
	                        where pizza.fk_pedido = pedido.id and pizza_ingrediente.fk_id_pizza = pizza.id AND
	                        pizza_ingrediente.fk_ti_tamano_ingrediente = tamano_ingrediente.fk_tamano and 
	                        tamano_ingrediente.fk_ingrediente = ingrediente.id and pizza_ingrediente.fk_ti_ingrediente=tamano_ingrediente.fk_ingrediente
	                        group by pedido.fecha_pedido, tamano_ingrediente.precio_ingrediente,
	                        ingrediente.nombre_ingrediente) as pedidos_ingredientes
                            group by pedidos_ingredientes.fecha_pedido, pedidos_ingredientes.nombre_ingrediente ''').fetchall()
    return vent_ing

def printTables():
    cur = CONNECTION.cursor()

    '''Muestra los datos de Pedido'''
    print("Datos del Pedido")
    cur.execute('''SELECT * FROM pedido''')
    rows = cur.fetchall()
    print("--------------------------")
    print("ID  |","F_Pedido |", "N_Cliente")
    print("--------------------------")
    for row in rows:
        print("{} {} {}".format(row[0], "   "+row[1], row[2]))
    print('\n')

    '''Muestra los datos de Tamano'''
    print("Datos de la tabla Tamano")
    cur.execute('''SELECT * FROM tamano''')
    rows = cur.fetchall()
    print("-----------------------")
    print("ID  |","N_Tam    |", "C_Tam")
    print("-----------------------")
    for row in rows:
        print("{} {} {}".format(row[0], "   "+row[1]+"  ",row[2]))
    print('\n')

    '''Muestra los datos de Ingrediente'''
    print("Datos de tabla Ingrediente")
    cur.execute('''SELECT * FROM ingrediente''')
    rows = cur.fetchall()
    print("-----------------------")
    print("ID  |","N_Ingrediente    ")
    print("-----------------------")
    for row in rows:
        print("{} {}".format(row[0], "   "+row[1]))
    print('\n')
    
    '''Muestra los datos de Tamano_Ingrediente'''
    print("Datos de la tabla Tamano_Ingrediente")
    cur.execute('''SELECT * FROM tamano_ingrediente''')
    rows = cur.fetchall()
    print("-----------------------")
    print("Costo   |","ID.I   | ", "ID.T")
    print("-----------------------")
    for row in rows:
        print("{} {} {}".format(row[0], "    "+str(row[1])+"       ",row[2]))
    print('\n')

    '''Muestra los datos de Pizza'''
    print("Datos de la tabla Pizza")
    cur.execute('''SELECT * FROM pizza''')
    rows = cur.fetchall()
    print("------------------------------")
    print("ID.P  |","ID.Pe   | ", "ID.T  ")
    print("------------------------------")
    for row in rows:
        print("{} {} {}".format(row[0], "       "+str(row[1])+"          ",str(row[2])))
    print('\n')

    '''Muestra los datos de Pizza_Ingrediente'''
    print("Datos de la tabla Pizza_Ingrediente")
    cur.execute('''SELECT * FROM pizza_ingrediente''')
    rows = cur.fetchall()
    print("-----------------------------------")
    print("ID.P  |","ID.T   | ", "ID.T  |","ID.I")
    print("-----------------------------------")
    for row in rows:
        print("{} {} {} {}".format(row[0], "      "+str(row[1])+"         ",str(row[2])+"       ", str(row[3])))
    print('\n\n')
    val = input("presiona una tecla para continuar...")