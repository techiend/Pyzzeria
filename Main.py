from Herramientas import *

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
    print('\n')

if __name__ == "__main__":
    # print("MAIN")
    procesar('pedidos1.pz')
    procesar('pedidos2.pz')
    procesar('pedidos3.pz')
    write_file(filepath="resumen.pz")
       