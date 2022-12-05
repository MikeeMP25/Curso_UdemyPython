from tkinter import *
import tkinter as tk

panel = Tk() #Creamos el objeto de la libreria tkinter 
#Es para inicializar nuestra vista de usuario 

panel.title("Bienvenidos")#Es el titulo de mi ventana
panel.resizable(1,1)#para ajustar el tamaño de la ventana a voluntad de l usuario 
panel.iconbitmap(r'puntero.png')


#Ventana hijo 
frame=Frame(panel,width=480,height=320)#El tamaño de la ventanade inicio 
frame.pack(fill="both",expand=1)#El comportamiento del frame en el panel
frame.config(bg="blue")#es el color del frame
frame.config(bd=18)#Es el borde del frame    
frame.config(cursor="pirate")#El tipo de cursor en el area del frame
frame.config(relief="sunken")

#Ventana padre
panel.config(cursor="arrow")
panel.config(bg="black")#color de la pantalla del panel 
panel.config(bd=14)
panel.config(relief="ridge")



#Finalmente bucle de la aplicacion
panel.mainloop()#Es para ejecutar la interfaz grafica
