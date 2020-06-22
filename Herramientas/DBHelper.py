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
                                            nombre_ingrediente TEXT NOT NULL,
                                            precio_ingrediente REAL NOT NULL)''')
    # Tabla Pizza
    c1.execute('''CREATE TABLE IF NOT EXISTS pizza (id INT PRIMARY KEY NOT NULL,
                                        fk_pedido INT NOT NULL,
                                        fk_tamano INT NOT NULL,
                                        FOREIGN KEY (fk_pedido) REFERENCES pedido (id_pedido),
                                        FOREIGN KEY (fk_tamano) REFERENCES tamano (id_tamano))''')
    # Tabla Pizza_Ingrediente
    c1.execute('''CREATE TABLE IF NOT EXISTS pizza_ingrediente (fk_pizza INT NOT NULL,
                                                    fk_ingrediente INT NOT NULL,
                                                    FOREIGN KEY (fk_pizza) REFERENCES pizza (id_pizza),
                                                    FOREIGN KEY (fk_ingrediente) REFERENCES ingrediente (id_ingrediente))''')
    c1.close()
    # Esto es una prueba
    # c1.execute("INSERT INTO pizza (id_pizza) VALUES (1);")
    # conection.commit()
    # c2 = conection.execute("SELECT id_pizza FROM pizza;")
    # for row in c2:
    #     print("ID =",row[0])
    print("Tablas creadas exitosamente")
    return

def lastID(table):
    cur = CONNECTION.cursor()
    last = cur.execute(f"SELECT MAX(id) FROM {table}").fetchone()
    if last.__contains__("None"):
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

CONNECTION = create_connection("pyzzeria.sql")
create_tables()