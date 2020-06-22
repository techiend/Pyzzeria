import  sqlite3
import sqlite3 as lite
from sqlite3 import Error

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
    c1.execute('''CREATE TABLE IF NOT EXISTS tamano_ingrediente (precio_ingrediente REAL NOT NULL,
                                                                fk_ingrediente INT NOT NULL,
                                                                fk_tamano INT NOT NULL,
                                                                FOREIGN KEY (fk_ingrediente) REFERENCES ingrediente(id),
                                                                FOREIGN KEY (fk_tamano) REFERENCES tamano(id))''')
    # Tabla Pizza_Ingrediente
    c1.execute('''CREATE TABLE IF NOT EXISTS pizza_ingrediente (fk_id_pizza INT NOT NULL,
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
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (1, 1, 1.50)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (1, 2, 1.75)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (1, 3, 2.00)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (2, 1, 1.75)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (2, 2, 2.05)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (2, 3, 2.50)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (3, 1, 1.50)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (3, 2, 1.75)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (3, 3, 2.00)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (4, 1, 0.80)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (4, 2, 1.30)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (4, 3, 1.70)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (5, 1, 1.80)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (5, 2, 2.15)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (5, 3, 2.60)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (6, 1, 1.25)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (6, 2, 1.70)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (6, 3, 1.90)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (7, 1, 1.60)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (7, 2, 1.85)''')
        c1.execute('''INSERT INTO tamano_ingrediente (fk_ingrediente, fk_tamano, precio_ingrediente) VALUES (7, 3, 2.10)''')
        print("Rows (tamano_ingrediente) added successfully")
        CONNECTION.commit()
    else:
        print("- Skip the inserts (tamano_ingrediente) -")

    c1.close()
    print("Tables created successfully")
    return

def lastID(table):
    cur = CONNECTION.cursor()
    last = cur.execute(f"SELECT MAX(id) FROM {table}").fetchone()
    if last[0] == None:
        last = 1
    else:
        last = last[0] + 1
    return last

def addPedido(nombreCliente, fechaPedido):
    c1 = CONNECTION.cursor()
    idPedido = lastID("pedido")
    c1.execute('''INSERT INTO pedido (id, fecha_pedido, nombrecliente_pedido) 
                                        values (?, ?, ?)''',(idPedido, fechaPedido, nombreCliente))
    CONNECTION.commit() 
    print("Datos del Pedido insertado exitosamente")
    return idPedido

def addPizza(idPedido, tamano, ingredientes):
    cur = CONNECTION.cursor()
    idTamano = cur.execute(f'''SELECT id FROM tamano WHERE nombre_tamano = "{tamano}" ''').fetchone()
    idPizza = lastID("pizza")
    if idTamano == None:
        print("El tamaño ",tamano," no existe")
    else:
        cur.execute('''INSERT INTO PIZZA (id, fk_pedido, fk_tamano) VALUES (?, ?, ?)''',(idPizza, idPedido, idTamano[0]))
    
    for ing in ingredientes:
        idIngrediente = cur.execute(f'''SELECT id FROM ingrediente WHERE nombre_ingrediente = "{ing}" ''').fetchone()
        if idIngrediente == None:
            print("El ingrediente ",ing," no esta disponible")
            return 
        else:
            cur.execute('''INSERT INTO pizza_ingrediente (fk_id_pizza, fk_tamano_pizza, fk_ti_tamano_ingrediente, fk_ti_ingrediente) 
                                        VALUES (?, ?, ?, ?)''',(idPizza, idTamano[0], idTamano[0], idIngrediente[0]))
    CONNECTION.commit() 
    print("Pizza insertada exitosamente !")


CONNECTION = create_connection("pyzzeria.sql")
create_tables()