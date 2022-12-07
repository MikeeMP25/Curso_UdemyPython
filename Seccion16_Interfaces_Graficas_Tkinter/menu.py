from tkinter import *

root=Tk()

menubar=Menu(root)
root.config(menu=menubar)


filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="salir",command=root.quit)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="cortar")
editmenu.add_command(label="pegar")
editmenu.add_command(label="cortar")


helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo",menu=filemenu)
menubar.add_cascade(label="Editar",menu=editmenu)
menubar.add_cascade(label="Ayuda",menu=helpmenu)

Label(root,text="Bievenidos").pack()
root.mainloop()