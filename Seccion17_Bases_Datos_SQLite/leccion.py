#Conexion, puntero y consultas SQLite
import sqlite3

#Establecemos conexion con la base de datos "ejemplo.db" sino la crea
conexion=sqlite3.connect("ejemplo.db")
cursor=conexion.cursor()#creamos el cursor de la base de datos es como el puntero en ficheros

#Sentencia pra crear una tabla con sus repsctivos atritubos
#cursor.execute("CREATE TABLE usuarios (id INTEGER, nombre VARCHAR(100),edad INTEGER,email VARCHAR(100))")

#Sentencia de registro de un usuario en la tbla usuarios
#cursor.execute("INSERT INTO usuarios VALUES(2,'Jessy',25,'jess@gmail.com')")


"""
Es una sentencia de consulta de todos los registros de la tabla usuarios
cursor.execute("SELECT * FROM usuarios")

cursor.fechone obtiene el primer usuario y lo muestra
usuario=cursor.fetchone()
print(usuario)
cursor se movio y ahora esta con el segundo usuario y lo imprime
usuario=cursor.fetchone()
print(usuario)

Lista de usuarios
usuarios=[
    (3,'Maria',50,'maria_guadalupe@gmail.com'),
    (4,'Martha',35,'mariposa60@gmail.com'),
    (6,'Mayra',26,'karate_kitGirl@hotmail.com')
]

Este es un insert masivo de una lista 
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)",usuarios)
"""

#Es una sentencia de consulta de todos los registros que ahi en la tabla usuarios
cursor.execute("SELECT * FROM usuarios")
usuarios=cursor.fetchall()
for usuario in usuarios:
    print("Nombre: ",usuario[1]," Edad: ",usuario[2])


conexion.commit()#ESTE COMMIT ES PARA CONFIRMAR LOS CAMBIOS QUE TENDRA LA BASE DE DATOS (uusarios)

conexion.close()