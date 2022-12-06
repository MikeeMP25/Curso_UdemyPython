from tkinter import *

def hola():
    print("hola mundo")

def crear_label():
    Label(root,text="Label creada dinamicamente").pack()
    

root=Tk()

Button(root,text="clicame",command=hola).pack()

#Finalmente bucle de la aplicacion
root.mainloop()