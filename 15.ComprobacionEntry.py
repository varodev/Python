from tkinter import *
import datetime

def devolverAnio():
    hoy=datetime.datetime.now()
    anio=hoy.year
    return anio

def comprobar():
    hoy=datetime.datetime.now()
    
    cont=0
    nombre=entrada.get()
    text2="0123456789"
    for x in nombre:
        for y in text2:
            if x==y:
                cont=cont+1
    texto="Has insertado " + str(cont) + " cantidad de números.\n"
    texto+="La longitud es de " + str(len(nombre))+"\n"
    eti2['text']=texto
    anio2=devolverAnio()
    boton1['text']=anio2

ventana=Tk()
entrada=Entry(ventana,width=8,show="*")
etiqueta=Label(ventana,text="Inserta la contraseña")
eti2=Label(ventana,text="H")
boton1=Button(ventana, text="Comprobar", command=comprobar)
etiqueta.pack(pady=10)
entrada.pack(pady=10)
boton1.pack(pady=10)
eti2.pack(pady=10)

ventana.mainloop()
