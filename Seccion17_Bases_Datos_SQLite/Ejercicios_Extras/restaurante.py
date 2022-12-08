import sqlite3

#Esta funcion crea la base de datos y el contenido de la misma tablas y atributos  
def crear_bd():
    
    conexion=sqlite3.connect("Ejercicios_Extras/restaurante.db")
    cursor=conexion.cursor()

    try:
        cursor.execute('''
        CREATE TABLE categoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100)UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("la tabla de categoria ya existe.")
    else:
        print("La tabla de categorias se ha creado correctamente.")

    try:
        cursor.execute('''
        CREATE TABLE plato(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100)UNIQUE NOT NULL,
        categoria_id INTEGER NOT NULL,
        FOREIGN KEY(categoria_id)REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla plato ya existe.")
    else:
        print("la tabla de plato se ha creado correctamente")
    conexion.close()

#Esta funcion agrega una nueva categoria ala base de datos 
def agregar_categoria():
    new_category=input("¿Nombre de la nueva categoria?\n> ")
    conexion=sqlite3.connect("Ejercicios_Extras/restaurante.db")
    cursor=conexion.cursor()
    
    try:
        cursor.execute("INSERT INTO categoria VALUES (null,'{}')".format(new_category))
    except sqlite3.OperationalError:
        print("la categoria'{}' ya existe.".format(new_category))
    else:
        print("la categoria'{}' crerada correctamente.".format(new_category)) 

    conexion.commit()
    conexion.close()

#Esta funcion sirve para agregar un nuevo plato mediante la categoria en la base de datos restaurante.db
def agregar_plato():

    conexion=sqlite3.connect("Ejercicios_Extras/restaurante.db")
    
    cursor=conexion.cursor()
    cursor.execute("Select * from categoria")
    categorias=cursor.fetchall()
    print("Selecciona una categoria para añadir el plato:")
        
    for categoria in categorias:
        print("[{}] {}".format(categoria[0],categoria[1]))

    categoria_usuario=int(input(">")) 
    plato=input("Nombre del nuevo platillo: ")
    try:
        cursor.execute("INSERT INTO plato VALUES(null,'{}','{}')".format(plato,categoria_usuario))
    except sqlite3.OperationalError:
        print("El plato'{}' ya existe.".format(plato))
    else:
        print("El plato'{}' creado correctamente.".format(plato)) 

    conexion.commit()
    conexion.close()

#Esta funcion es una consulta de los registros de las tablas categoria y plato en la BD restaurante.db 
def mostrar_menu():
    print("""¡Bienvenidos a ChilisWills!
        La carta de casa
    """)
    conexion=sqlite3.connect("Ejercicios_Extras/restaurante.db")
    cursor=conexion.cursor()
    categorias=cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print("Categoria: ",categoria[1])
        platos=cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("\t\t\tPlato: {}".format(plato[1]))
            
    conexion.close()

#crear la base de datos3
crear_bd()

#Menu principal consola :3
#Menu operaciones del programa SQLite
while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion=int(input("\nIntroduce una opcion:\n[1] Agregar una Categoria.\n[2] Agregar un plato.\n[3] Mostrar menu.\n[4] Salir del programa.\n"))

    if opcion==1:
        agregar_categoria()
    elif opcion ==2:
        agregar_plato()

    elif opcion==3:
        mostrar_menu()

    elif opcion ==4:
        print("\nHasta la proxima")
        break
    else:
        print("\nOpcion incorrecta...!")



