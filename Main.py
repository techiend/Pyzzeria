from Herramientas import *

def read_and_write():
    # Para leer los archivos
    create_tables()
    conection = create_connection()
    c1 = conection.cursor()
    idP = 0
    i = 1

    t = os.path.isfile("pedidos1.pz")
    if (t == True):
        with open("pedidos1.pz", "r") as f:
            f1 = f.readlines()
            for x in f1:
                if x.startswith("COMIENZO_PEDIDO"):
                    idP +=1
                    print("ID_Pedido = ",idP)
                if x.__contains__("/"):
                    separa = x.split(";")
                    nombre = separa[0]
                    fecha = separa[1]
                    print("Nombre cliente =", nombre)
                    print("Fecha pedido =", fecha.strip())
                if (x.startswith("personal") or x.startswith("familiar") or x.startswith("mediana")):
                    if x.__contains__(";"):
                        ingr = x.split(";")
                        tamano = ingr[0]
                        print("Tamano = ", tamano)
                        if (tamano == "personal"):
                            costo = 10
                            print("Costo x tamano = ", costo)
                            for ingrendiente in ingr[1:]:
                                # ingrendiente = ingr[i]
                                print("Ingrediente = ", ingrendiente.strip())
                        if (tamano == "mediana"):
                            costo = 15
                            print("Costo x tamano = ", costo)
                            for ingrendiente in ingr[1:]:
                                # ingrendiente = ingr[i]
                                print("Ingrediente = ", ingrendiente.strip())
                        if (tamano == "familiar"):
                            costo = 20
                            print("Costo x tamano = ", costo)
                            for ingrendiente in ingr[1:]:
                                # ingrendiente = ingr[i]
                                print("Ingrediente = ", ingrendiente.strip())
                    else: 
                        tamano = x[0:].strip()
                        print("Tamano =", tamano)
                        if (tamano == "personal"):
                            costo = 10
                            print("Costo x tamano = ", costo)
                        if (tamano == "mediana"):
                            costo = 15
                            print("Costo x tamano = ", costo)
                        if (tamano == "familiar"):
                            costo = 20
                            print("Costo x tamano = ", costo)

                if x.startswith("FIN_PEDIDO"):
                    print("FINNNNN")
    else:
        print("ERRROR \n¡¡ El archivo no existe !!")


if __name__ == "__main__":
    print("MAIN")
    read_and_write()
    # create_tables()
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
    # main()