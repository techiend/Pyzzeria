from Herramientas import *

def clearScreen():
    ''' Metodo encargado de limpiar la pantalla usando
    el comando tipico para ello dependiendo del SO '''
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cargar():
    ''' Metodo encargado de recibir el PATH donde se supone
    esta ubicado el archivo de pedido a cargar '''
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
                clearScreen()
                printTables()
            elif (opcion == 0):
                clearScreen()
                input("Saliendo de Pyzzeria!\n\nPresiona una tecla para cerrar...")
                break
            else:
                clearScreen()
        except ValueError:
            pass
       
