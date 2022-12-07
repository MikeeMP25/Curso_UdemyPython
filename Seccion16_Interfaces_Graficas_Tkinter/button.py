from tkinter import *


#debes de crear la funcion antes de mandarlo a llamar 
def hola():
    print("hola mundo")

def crear_label():
    Label(root,text="Label creada dinamicamente").pack()
    #EL PACK SIEMPRE TIENE QUE IR AL CREAR UN NUEVO ELEMENTO (EMPAQUETAR)
    
#Espara crear un boton en la raiz 
#Button(root,text="clicame",command=crear_label).pack()
#NOTA: CUANDO MANDEMOS A LLAMAR A LA FUNCION CREAR_LABEL EL ROOT 
# YA ESTARA CREADO Y NO HABRA PROBLEMAS
def suma():
    result.set( float(n1.get()) + float(n2.get()) )
    vaciar()

def resta():
    result.set(float(n1.get())-float(n2.get()))
    vaciar()

def multiplica():
    result.set(float(n1.get())*float(n2.get()))
    vaciar()


def vaciar():
    n1.set("")
    n2.set('')




root=Tk()
#Variables
n1=StringVar()
n2=StringVar()
result=StringVar()

#LA VISTA AL USUARIO
label=Label(root,text="Ingresa un numero: ")
label.grid(row=0,column=0,sticky="w")

entry=Entry(root,textvariable=n1 )
entry.grid(row=0,column=1)
entry.config(justify="right")

label2=Label(root,text="Ingresa otro numero:")
label2.grid(row=1,column=0,sticky="w")

entry2=Entry(root, textvariable=n2)
entry2.grid(row=1,column=1)
entry.config(justify="right")

boton=Button(root, text="Sumar",command=suma)
boton.grid(row=2,column=0)
boton=Button(root, text="Restar",command=resta)
boton.grid(row=2,column=1)
boton=Button(root, text="Multiplicar",command=multiplica)
boton.grid(row=2,column=2)

entry3=Entry(root,textvariable=result)
entry3.grid(row=3,column=1, padx=5, pady=5)
entry3.config(justify="right", state="disabled")

#Finalmente bucle de la aplicacion
root.mainloop()