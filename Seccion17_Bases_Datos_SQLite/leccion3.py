import sqlite3

conexion=sqlite3.connect("usuarios_autoincrement.db")
cursor=conexion.cursor()

#cursor.execute("SELECT * FROM usuarios WHERE dni='as1a25x13'")
#usuario=cursor.fetchone()
#print(usuario)

#cursor.execute("UPDATE usuarios SET nombre='Jesus Miranda',edad=27 WHERE dni='as1a25x13'")

#cursor.execute("UPDATE usuarios SET email='jesus.libra619@gmail.com' WHERE dni='as1a25x13'")

cursor.execute("DELETE FROM usuarios WHERE dni='as1a25x13'")

conexion.commit()
conexion.close()