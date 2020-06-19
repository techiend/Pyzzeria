import os

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