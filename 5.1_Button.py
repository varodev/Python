from tkinter import *

estado = 0

def cambiaEtiqueta():
    global estado
    if estado == 0:
        print(estado)
        etiquet1=Label(ventana, text="Label 2")
        etiquet1.grid(column=0, row=0)
        estado = 1
    else:
        print(estado)
        etiquet1=Label(ventana, text="Label 1")
        etiquet1.grid(column=0, row=0)
        estado = 0

ventana=Tk()
ventana.title("Ejemplo de etiqueta con boton")
ventana.geometry("400x200")
etiquet1=Label(ventana, text="Label 1")
etiquet1.grid(column=0, row=0)
boton1=Button(ventana, text="Click me",command=cambiaEtiqueta)
boton1.grid(column=0, row=1)


ventana.mainloop()
