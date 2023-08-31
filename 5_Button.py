from tkinter import *


def cambiaEtiqueta():
       etiquet1=Label(ventana, text="Etiqueta Cambiada")
       etiquet1.grid(column=0, row=0)

ventana=Tk()
ventana.title("Ejemplo de etiqueta con boton")
ventana.geometry("400x200")
etiquet1=Label(ventana, text="Label 1")
etiquet1.grid(column=0, row=0)
boton1=Button(ventana, text="Click me",command=cambiaEtiqueta)
boton1.grid(column=0, row=1)


ventana.mainloop()
