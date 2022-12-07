from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")

root=Tk()
opcion=IntVar()

#la estructura de configuracion de un radio button es 
# raiz / nombre / variable donde se guardara y manipulara los datos / se le asigna un valor / manda a llamar una funcion / el pack de ley 
Radiobutton(root,text="Opcion 1", variable=opcion, value=1,command=seleccionar).pack()
Radiobutton(root,text="Opcion 2", variable=opcion, value=2,command=seleccionar).pack()
Radiobutton(root,text="Opcion 3", variable=opcion, value=3, command=seleccionar).pack()

monitor=Label(root)
monitor.pack()

#la estructura de configuracion de un button es
#raiz/ nombre/manda a llamar una funcion/ el pack empaquete el contendio del button para mostrarlo en la raiz = root
Button(root,text="Limpiar",command=reset).pack()

root.mainloop()