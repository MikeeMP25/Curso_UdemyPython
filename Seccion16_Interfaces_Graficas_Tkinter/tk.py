"""
Bienvenidos a la interface grafica de tkinder en python   
Generaremos la interfaz grafica desde codigo python 
"""
from tkinter import *
import tkinter as tk

root = Tk() #Creamos el objeto de la libreria tkinter 
#Es para inicializar nuestra vista de usuario 

root.title("Bienvenidos")#Es el titulo de mi ventana

#root.iconbitmap("hola.ico")#para cargar un imagen en el icono de la ventana

root.geometry("400x500")#tamaño de la ventana 
icono_chico=tk.PhotoImage(file="/Users/Desarrollo/Devolopment/python/pokemon/Curso_UdemyPython/Seccion16_Interfaces_Graficas_Tkinter/Imagen/puntero.png")

#Este icono se coloca en la barra desplegable de tareas 
icono_grande=tk.PhotoImage(file="/Users/Desarrollo/Devolopment/python/pokemon/Curso_UdemyPython/Seccion16_Interfaces_Graficas_Tkinter/Imagen/puntero.png")

root.iconphoto(False,icono_grande,icono_chico) 
"""/Users/Desarrollo/Devolopment/python/pokemon/Curso_UdemyPython/Seccion16_Interfaces_Graficas_Tkinter/Imagen/pluma.png"""
root.resizable(True,True)#para ajustar el tamaño de la ventana a voluntad de l usuario 

root.mainloop()#Es para ejecutar la interfaz grafica

