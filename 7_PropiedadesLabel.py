from tkinter import *


def cambiaEtiqueta():
       #etiquet1=Label(ventana, text="Etiqueta Cambiada")
       etiquet1['text']="ADIOS"
       etiquet1['anchor']=NW
       etiquet1['borderwidth']=10
       etiquet1['relief']="sunken"  #tipo de borde
       

ventana=Tk()
ventana.title("Ejemplo de etiqueta con boton")
ventana.geometry("400x500")
etiquet1=Label(ventana, text="Label 1",bg="yellow",relief="solid",height=20,width=40)
etiquet1.grid(column=0, row=0)
boton1=Button(ventana, text="Click me",command=cambiaEtiqueta)
boton1.grid(column=0, row=1)


ventana.mainloop()
