from tkinter import *

def seleccionar():
    cadena=""
    if(leche.get()):
        cadena+=" Leche"
    else:
        cadena+=" Sin leche"    
    
    if(azucar.get()):
        cadena+=" y con azucar"
    else:
        cadena+=" y sin azucar"    
    monitor.config(text=cadena)

#Configuracion de la raiz
root=Tk()

root.title("Cafeteria")
root.config(bd=15)

leche=IntVar() # 1 si, 0 no 
azucar=IntVar() # 1 si, 0 no

imagen=PhotoImage(file="Imagen/imagen.gif")
Label(root,image=imagen).pack(side="left")

frame=Frame(root)
frame.pack(side="right")

Label(frame,text="¿Como quieres el cafe?").pack(anchor="w")
#Configuracion del checkbutton
#raiz/nombre de ckeckbutton usuario/id de varible para get y set/ primer valor/segundo valor por defecto/la funcion a ejecutar/pack empaquetar el check
Checkbutton(frame,text="Con leche",variable=leche,onvalue=1,offvalue=0,command=seleccionar).pack(anchor="w")
Checkbutton(frame,text="Con azucar",variable=azucar,onvalue=1,offvalue=0,command=seleccionar).pack(anchor="w")

monitor=Label(frame)
monitor.pack()

#finalmente bucle de la aplicacion 
root.mainloop()