import datetime
from tkinter import *
from tkinter.ttk import *

hoy=datetime.datetime.now()
anio=hoy.year

def enviar ():
    dato=micombo.get()
    etiq["text"]=dato



ventana=Tk()
ventana.title("Ejercicio Combobox")

formulario=Frame(ventana)
formulario.pack(pady=18,padx=10)


label=Label(formulario,
            text="Año de nacimiento")
label.grid(column=0, row=0)

micombo=Combobox(formulario)
micombo["values"]=(anio-30,anio-29,anio-28,anio-27,anio-26,
                   anio-25,anio-24,anio-23,anio-22,anio-21,
                   anio-20,anio-19,anio-18)
micombo.current(12)
micombo.grid(column=1, row=0)

botones=Frame(ventana)
botones.pack(pady=9)

boton=Button(botones,
             text="Enviar",
             command=enviar)

boton.pack()

etiq= Label(botones, text= " ")
etiq.pack(pady=15)
