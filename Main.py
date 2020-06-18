import  sqlite3
from sqlite3 import Error
import os

def create_connection():
    #  Crear coneccion de la bd que se aloja en memoria
    conn = None
    try: 
        # conn = sqlite3.connect(":memory:")
        conn = sqlite3.connect("pyzzeria.sql")
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()

    return conn

def main():
    # Para leer los archivos
    t = os.path.isfile("pedidos1.pz")
    if (t == True):
        f = open("pedidos1.pz", "r")   
        # if f.mode == "r":
        #     contenido = f.read()
        #     print(contenido)
        f1 = f.readlines()
        for x in f1:
            print(x)
        f.close()
    else:
        print("ERRROR \n¡¡ El archivo no existe !!")

def create_tables():
    conection = create_connection()
    c1 = conection.cursor()
    # Tabla Pedido
    c1.execute('''CREATE TABLE IF NOT EXISTS pedido (id_pedido INT PRIMARY KEY NOT NULL,
                                        fecha_pedido TEXT NOT NULL,
                                        nombrecliente_pedido TEXT NOT NULL)''')
    # Tabla Tamaño
    c1.execute('''CREATE TABLE IF NOT EXISTS tamano (id_tamano INT PRIMARY KEY NOT NULL,
                                        nombre_tamano TEXT NOT NULL,
                                        costo_tamano REAL NOT NULL)''')
    # Tabla Ingrediente
    c1.execute('''CREATE TABLE IF NOT EXISTS ingrediente (id_ingrediente INT PRIMARY KEY NOT NULL,
                                            nombre_ingrediente TEXT NOT NULL,
                                            precio_ingrediente REAL NOT NULL)''')
    # Tabla Pizza
    c1.execute('''CREATE TABLE IF NOT EXISTS pizza (id_pizza INT PRIMARY KEY NOT NULL,
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

if __name__ == "__main__":
    create_tables()
    # conection = create_connection()
    # conn = sqlite3.connect(':memory:')
    # c1 = conection.cursor()
    # c1.execute('''CREATE TABLE pizza (id_pizza int primary key not null)''')
    # c1.execute("INSERT INTO pizza (id_pizza) VALUES (1);")
    # conection.commit()
    # c2 = conection.execute("SELECT id_pizza FROM pizza;")
    # for row in c2:
    #     print("ID =",row[0])
    # conn.execute('''CREATE TABLE pizza (id_pizza int primary key not null)''')
    # conn.execute("INSERT INTO pizza (id_pizza) VALUES (1)")
    # conn.commit()
    # cursor = conn.execute("SELECT id_pizza FROM pizza")
    # for row in cursor:
    #     print("ID = ", row[0])
    #main()