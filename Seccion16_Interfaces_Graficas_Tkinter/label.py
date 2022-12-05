from tkinter import *

# Configuracion de la raiz 
root=Tk()

# configuracion de un marco
frame=Frame(root,width=480,height=320)
frame.pack()

label=Label(frame,text="¡Hola mundo!")
#label.pack()#El pack empaqueta y distribuye a su manera
# entonces lo que queremos es posicionarlo en un lugar que no se mueva coordenas x & y   
label.place(x=100,y =100)#son las coordenas x y del plano 

#Finalmente bucle de la aplicación
root.mainloop()