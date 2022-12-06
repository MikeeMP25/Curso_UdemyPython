from tkinter import *

# Configuracion de la raiz 
root=Tk()

# configuracion de un marco
#frame=Frame(root,width=480,height=320)
#frame.pack()

#label=Label(frame,text="¡Hola mundo!")#Para poner un poco de texto en la ventana
#label.pack()#El pack empaqueta y distribuye a su manera
# entonces lo que queremos es posicionarlo en un lugar que no se mueva coordenas x & y   
#label.place(x=100,y =100)#son las coordenas x y del plano 


#texto=StringVar()#El string var para cambiar el contenido 
#texto.set("Un nuevo texto")
"""
#Lo hacemos mas directo sobre la misma clase 
Label(root, text="¡Hola mundo!").pack(anchor="nw")#agregamos texto a label y posicion
label=Label(root,text="¡Otra etiqueta!")
label.pack(anchor="center")
Label(root, text="Ultima etiqueta").pack(anchor="se")#agregamos texto a label y poscion

label.config(bg="green",fg="blue",font=("Verdana",24))#le damos el formato del texto de label
#label.config(textvariable=texto)
"""
#Para cargar una imagen en el label utilizamos lo siguiente
imagen=PhotoImage(file="Imagen/puntero.png")
Label(root, text="¡Hola mundo!").pack(anchor="nw")
Label(root,image=imagen,bd=0).pack(side="left")

#el pack() se hacer despues de escribir en el objeto su funcion es empaquetar lo que ahi


#Finalmente bucle de la aplicación
root.mainloop()