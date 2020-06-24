from Herramientas import *

def printTables():
    clearScreen()
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

    print("Datos de la tabla Tamano")
    '''Muestra los datos de Tamano'''
    cur.execute('''SELECT * FROM tamano''')
    rows = cur.fetchall()
    print("-----------------------")
    print("ID  |","N_Tam    |", "C_Tam")
    print("-----------------------")
    for row in rows:
        print("{} {} {}".format(row[0], "   "+row[1]+"  ",row[2]))
    print('\n')

    print("Datos de tabla Ingrediente")
    '''Muestra los datos de Ingrediente'''
    cur.execute('''SELECT * FROM ingrediente''')
    rows = cur.fetchall()
    print("-----------------------")
    print("ID  |","N_Ingrediente    ")
    print("-----------------------")
    for row in rows:
        print("{} {}".format(row[0], "   "+row[1]))
    print('\n')
    
    print("Datos de la tabla Tamano_Ingrediente")
    '''Muestra los datos de Tamano_Ingrediente'''
    cur.execute('''SELECT * FROM tamano_ingrediente''')
    rows = cur.fetchall()
    print("-----------------------")
    print("Costo   |","ID.I   | ", "ID.T")
    print("-----------------------")
    for row in rows:
        print("{} {} {}".format(row[0], "    "+str(row[1])+"       ",row[2]))
    print('\n')

    print("Datos de la tabla Pizza")
    '''Muestra los datos de Pizza'''
    cur.execute('''SELECT * FROM pizza''')
    rows = cur.fetchall()
    print("------------------------------")
    print("ID.P  |","ID.Pe   | ", "ID.T  ")
    print("------------------------------")
    for row in rows:
        print("{} {} {}".format(row[0], "       "+str(row[1])+"          ",str(row[2])))
    print('\n')

    print("Datos de la tabla Pizza_Ingrediente")
    '''Muestra los datos de Pizza_Ingrediente'''
    cur.execute('''SELECT * FROM pizza_ingrediente''')
    rows = cur.fetchall()
    print("-----------------------------------")
    print("ID.P  |","ID.T   | ", "ID.T  |","ID.I")
    print("-----------------------------------")
    for row in rows:
        print("{} {} {} {}".format(row[0], "      "+str(row[1])+"         ",str(row[2])+"       ", str(row[3])))
    print('\n\n')
    val = input("presiona una tecla para continuar...")

def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cargar():
    clearScreen()
    print("---------OPCION---------")
    print("   1. Cargar pedido     ")
    print("---------OPCION---------\n")
    path = input("Ingresa el path del archivo a cargar: ")
    arch = os.path.isfile(path)
    if arch == True:
        procesar(path)
    else:
        print(F"Lo siento, el archivo especificado no se encuentra.")
    val = input("\n\nPresiona una tecla para continuar...")

if __name__ == "__main__":
    # print("MAIN")
    # procesar('pedidos1.pz')
    # procesar('pedidos2.pz')
    # procesar('pedidos3.pz')

    while True:
        clearScreen()
        print("----------MENU----------")
        print("   1. Cargar pedido     ")
        print("   2. Generar resumen   ")
        print("   3. Select tablas     ")
        print("                        ")
        print("   0. Salir             ")
        print("----------MENU----------\n")
        try:
            opcion = int(input("Introduce una opcion: "))
            
            if (opcion == 1):
                cargar()
            elif (opcion == 2):
                clearScreen()
                write_file(filepath="resumen.pz")
                val = input("\n\nPresiona una tecla para continuar...")
            elif (opcion == 3):
                printTables()
            elif (opcion == 0):
                clearScreen()
                input("Saliendo de Pyzzeria!\n\nPresiona una tecla para cerrar...")
                break
            else:
                clearScreen()
        except ValueError:
            pass
       
