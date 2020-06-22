from Herramientas import *

if __name__ == "__main__":
    # print("MAIN")
    read_and_write()
    print('\n')
    addPedido("Maria Perez","03/02/2020")
    cur = CONNECTION.cursor()
    cur.execute('''SELECT * FROM pedido''')
    rows = cur.fetchall()
    print("--------------------------")
    print("ID  |","F_Pedido |", "N_Cliente")
    print("--------------------------")
    for row in rows:
        print("{} {} {}".format(row[0], "   "+row[1], row[2]))
    print('\n')
    
    
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