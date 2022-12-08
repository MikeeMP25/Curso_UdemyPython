import sqlite3

conexion=sqlite3.connect("usuarios_autoincrement.db")
cursor=conexion.cursor()

#cursor.execute("""
 #   'CREATE TABLE usuarios(
  #      id VARCHAR(9) PRIMARY KEY,
  #      nombre VARCHAR(100),
   #     edad INTEGER,
    #    email VARCHAR(100) 
    #)
   # """)
"""
usuarios=[
    ("a123s1a3b",'Hector',48,'hector_2015@gmail.com'),
    ("213231aas",'Maria',20,'maria@gmail.com'),
    ("a23sa1av3",'Mario',21,'mario_20151@gmail.com'),
    ("as1a25x13",'Martha',35,'mariposa60@gmail.com'),
    ("ads3df231",'Mayra',26,'karate_kitGirl@hotmail.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)",usuarios)
"""

#cursor.execute('''
#    CREATE TABLE productos(
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        nombre VARCHAR(100)NOT NULL,
#        marca VARCHAR(50) NOT NULL,
#        precio FLOAT NOT NULL
#    )
#    ''')
"""
productos=[
    ("Papas","Sabritas",20.50),
    ("Madarina","Pepsi",15.50),
    ("Delice","kinder",20.50),
    ("Cacahuates","Japones",18.50),
    ("Chocolate","Emanes",25.50),
    ]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)

cursor.execute("SELECT * FROM productos")

productos=cursor.fetchall()
for producto in productos:
    print(producto)
"""

cursor.execute("""
   CREATE TABLE usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100) 
    )
    """)

usuarios=[
    ("a123s1a3b",'Hector',48,'hector_2015@gmail.com'),
    ("213231aas",'Maria',20,'maria@gmail.com'),
    ("a23sa1av3",'Mario',21,'mario_20151@gmail.com'),
    ("as1a25x13",'Martha',35,'mariposa60@gmail.com'),
    ("ads3df231",'Mayra',26,'karate_kitGirl@hotmail.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (NULL,?,?,?,?)",usuarios)



conexion.commit()#para aplicar los cambios en la base de datos 
conexion.close()#cerrar la conexion con la base de datos