from tkinter import *
from tkinter import messagebox

def click():
    
      #respuesta=messagebox.askquestion('Título de mensaje', 'Cuestion: Yes o no')
      #respuesta=messagebox.askyesno('Título de mensaje', 'Cuestion: True (1) o false(0)')
      #respuesta=messagebox.askyesnocancel('Título de mensaje', 'Cuestion: True (1) o false(0) o none ')
      #respuesta=messagebox.askokcancel('Título de mensaje', 'Cuestion: Aceptar o Cancelar ')
      respuesta=messagebox.askretrycancel('Título de mensaje', 'Reintentar o Cancelar')
      etiqueta['text']=respuesta
       
ventana=Tk()
ventana.title("Caja de mensajes")

etiqueta= Label(ventana,text="")
etiqueta.pack(padx=20,pady=10)
boton=Button(ventana,text="Hazme click",command=click)
boton.pack(pady=20,padx=20)


