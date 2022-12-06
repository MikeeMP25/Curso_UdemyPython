from tkinter import *

#configuracion de la raiz
root=Tk()
"""
frame=Frame(root)
frame.pack()

entry=Entry(frame)
entry.pack(side="right")
label=Label(frame, text="Nombre:   " )
label.pack(side="left")

frame2=Frame(root)
frame2.pack()

entry2=Entry(frame2)
entry2.pack(side="right")
label2=Label(frame2, text="Apellidos: " )
label2.pack(side="left")
"""
#COLOCAR LAS ETIQUETAS EN UNA TABLA LE DA UN FORMATO MAS DECENTE Y BIEN POSICIONADO
label=Label(root,text="Usuario:")
label.grid(row=0,column=0,sticky="w",padx=5,pady=5)#el formato de la celda label

entry=Entry(root)
entry.grid(row=0,column=1,padx=5,pady=5)#el formato de la celda del input
entry.config(justify="right",state="disabled")


label2=Label(root,text="Contaseña:")
label2.grid(row=1,column=0,sticky="w",padx=5,pady=5)#el formato de la celda label


entry2=Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5)#el formato de la celda del input2
entry2.config(justify="right",show="*")
#Finalmente bucle de la aplicicacion
root.mainloop()
