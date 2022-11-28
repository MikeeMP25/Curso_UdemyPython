#Nota: Para poder hacer esto es necesario estar dentro del mismo directorio Modulo
#import=hace referencia a todo lo que ahi en mi modulo saludos
#import saludos #estamos importando todo lo que ahi en el modulo hasta las deficiones
#al importan ejecutamos el codigo del otro modulo saludos


#podemos importar solo la funcion saludar de saludos mediante el siguiente codigo
#from saludos import saludar
#saludar() en efecto lo puede mandar a llamar esta deficion de saludos

#aqui podemos importar tambien variables del modulo de saludos
#from saludos import mensaje
#print(mensaje)

#Tenemos acceso a todas las definiciones del fichero saludos
from saludos import * 

#saludos.saludar()
"""
este se utiliza para comentar por bloque 
"""
saludar()
Saludo()