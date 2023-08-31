# VERSIÓN CON 2 IMÁGENES Y 2 BOTONES


from tkinter import *

estado=0

def cambiar():
    global estado
    if estado==0:
        etiqueta2.place(x=200,y=160)
        etiqueta.place(x=4000,y=4000)
        boton2.place(x=220,y=400)
        boton.place(x=4000,y=4000)
        estado=1
    else:
        etiqueta.place(x=200,y=160)
        etiqueta2.place(x=4000,y=4000)
        boton.place(x=220,y=400)
        boton2.place(x=4000,y=4000)
        estado=0




ventana=Tk()
ventana.title("Ejercicio 2. Lámpara")
ventana.geometry("500x500")

imagenApagada= PhotoImage(file="images/pic_bulboff.gif")
imagenEncendida = PhotoImage(file="images/pic_bulbon.gif")

etiqueta=Label(ventana,image=imagenApagada)
etiqueta.place(x=200,y=160)

etiqueta2=Label(ventana,image=imagenEncendida)
etiqueta2.place(x=4000,y=4000)


boton=Button(ventana,text="ENCENDER",command=cambiar)
boton.place(x=220,y=400)

boton2=Button(ventana,text="  APAGAR  ",command=cambiar)
boton2.place(x=4000,y=4000)

ventana.mainloop()
