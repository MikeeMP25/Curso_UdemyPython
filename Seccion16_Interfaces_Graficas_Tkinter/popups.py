#ventas emergentes 
from tkinter import *
from tkinter import messagebox as Messagefox
from tkinter import colorchooser as Colorchooser 
from tkinter import filedialog as FileDialog

root=Tk()

def test():
    #Messagefox.showinfo("Hola","Hola mundo")
    #Messagefox.showwarning("Alerta","Session sola para administradores ")
    #Messagefox.showerror("Error!","Ha ocurrido un error inesperado.")
    
    #resultado=Messagefox.askquestion("salir","Estas seguro de salir sin guardar?")
    #if resultado=="yes":
    #   root.destroy()
    #resultado=Messagefox.askokcancel("salir","¿Sobreescribir el ficehro acutal?")
    #resultado=Messagefox.askyesno("salir","¿Sobreescribir el ficehro acutal?")
    #if resultado:
    #    root.destroy()
    #resultado=Messagefox.askretrycancel("Reintentar","No se puede conectar")
    #if resultado:
    #    root.destroy()
    #color=Colorchooser.askcolor(title="Elige un color")
    #print(color)
    #ruta=FileDialog.askopenfilename(title="Abrir un fichero",initialdir="C:",
    #         filetypes=(("Fichero de texto",".txt"),
    #         ("Fichero de texto avanzado","*.txt2"),
    #        ("Todos los ficheros","*.*"))) 
    #print(ruta)

    fichero=FileDialog.asksaveasfile(title="guardar un fichero",mode="w",defaultextension= ".txt")
    if fichero is not None:
        fichero.write("Hola voy a escribir otra cosa!")
        fichero.close()



Button(root,text="Clicame",command=test).pack()



root.mainloop()