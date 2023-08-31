# VERSIÓN DE 1 IMAGEN Y 1 BOTÓN

from tkinter import *

estado=0

def cambiar():
    global estado
    if estado==0:
        etiqueta=Label(ventana,image=imagenEncendida).place(x=200,y=160)
        boton=Button(ventana,text="   APAGAR  ",command=cambiar).place(x=220,y=400)
        estado=1
    else:
        etiqueta=Label(ventana,image=imagenApagada).place(x=200,y=160)
        boton=Button(ventana,text="ENCENDER",bg="black",command=cambiar).place(x=220,y=400)
        estado=0




ventana=Tk()
ventana.title("Ejercicio 2. Lámpara")
ventana.geometry("500x500")

imagenApagada= PhotoImage(file="images/pic_bulboff.gif")
imagenEncendida = PhotoImage(file="images/pic_bulbon.gif")

etiqueta=Label(ventana,image=imagenApagada).place(x=200,y=160)

boton=Button(ventana,text="ENCENDER",command=cambiar).place(x=220,y=400)

ventana.mainloop()
