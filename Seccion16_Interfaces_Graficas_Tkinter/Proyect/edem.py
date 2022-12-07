import tkinter as tk
from tkinter import filedialog as FileDialog 
from io import open

ruta="" # la utilizaremos para almacenar la ruta del fichero

#funcion de carga de venta
def nuevo():
    global ruta #este es una variable global hace referencia a ruta 
    mensaje.set("Nuevo Fichero")
    ruta = ""
    texto.delete(1.0,"end")
    ventana.title("Mi editor")
    
#Funcion la utilizo para abrir un archivo .txt y mostrarlo en mi campo de texto 
def abrir():
    global ruta
    mensaje.set("Abrir fichero")#mensaje de label
    ruta=FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("Ficheros de texto","*.txt"),),
        title="Abrir un fichero de texto")# para verificar que la ruta esta correcta
    
    if ruta!="":#valido que la ruta no este vacia
        fichero=open(ruta,"r")#para abrir el fichero en modo lectura
        contenido=fichero.read()#obtengo el contendio del fichero
        texto.delete(1.0,"end")#limpio mi campo de texto antes de mostrar el contenido 
        texto.insert('insert',contenido)#ahora muestro en contendio en mi campo de texto
        fichero.close()#RECUERDA SI ESTAS TRABAJANDO CON FICHEROS SE RECOMIENDA CERRAR EL FICHERO AL FINALIZAR OPERACIONES DENTRO DEL MISMO
        ventana.title(ruta + "- Mi editor")#Le asigno la ruta en donde proviene ese fichero

#Funcion la utilizo para guardar un archivo .txt y tambien guardo el contenido de texto en el archivo
def guardar():
    mensaje.set("Guardar fichero")#Mensaje del label que operacion estoy realizando 
    if ruta !="": #Valido si la ruta esta establecida con algo que no e sta vacia
        contenido=texto.get(1.0,'end-1c')#obtengo todos los datos de mi caja de texto y lo guardo en mi variable contenido
        fichero=open(ruta,"w+")#abro el fichero con el que estoy trabajando mediante la ruta en forma de lectura y escritura esto abre y el fichero y limpia el contenido
        fichero.write(contenido)#almaceno la nueva informacion de mi varible contenido en el fichero.txt
        fichero.close()#cerrar fichero
        texto.delete(1.0,"end")#limpio la caja de texto
        mensaje.set("Fichero guardado correctamente")#mando un mensaje de confirmacion que todo salio bien
        
    else:#Valido si la ruta esta vacia va genera un nuevo fichero.txt con la informacion de la caja de texto
        guardar_como()#Manda a llamar a mi funcion guardar como
        texto.delete(1.0,"end")#    

#Esta funcion se encarga de guardar un nuevo archivo.txt con su contenido  
def guardar_como():
    mensaje.set("Guardar como fichero")#mensaje de label superior guardar uno nuevo fichero
    global ruta#hace referecnia a mi varible global ruta 
    fichero=FileDialog.asksaveasfile(title="Guardar fichero",mode="w",defaultextension=".txt")#aqui abrimos nuestro adminitrador de archivo con algunas especificaciones
    if fichero is not None:#validamos que el fichero no sea null
        ruta=fichero.name#le vamos a mandar la ruta del fichero junto con /nombre.txt  
        contenido=texto.get(1.0,'end-1c')#obtenemos los datos del la caja de texto 
        fichero=open(ruta,"w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")#Mensaje de confirmacion
    else:
        mensaje.set("Guardado cancelado")#Mensaje de cancelacion 
        ruta=""

#Configuracion de la raiz
ventana=tk.Tk()
ventana.title("Mi editor")
ventana.config(width=400,height=300)

#Menu superior
menubarr=tk.Menu()
filemenu=tk.Menu(menubarr,tearoff=False)
menubarr.add_cascade(menu=filemenu, label="Archivo")

#Menu menubarr 
filemenu.add_command(label="Nuevo",command=nuevo)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=ventana.quit)
menubarr.add_cascade(menu=filemenu)

#caja de texto central
texto=tk.Text(ventana)
texto.pack(fill="both",expand=1)
texto.config(bd=0,padx=6,pady=4,font=("Consolas",12))

#Label Monitor inferior
mensaje=tk.StringVar()
mensaje.set("Bienvenido a tu editor")
monitor=tk.Label(ventana,textvar=mensaje,justify='left')
monitor.pack(side="left")

#Finalmente bucle de la aplicacion 
ventana.config(menu=menubarr)
ventana.mainloop()
