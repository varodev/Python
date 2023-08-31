from tkinter import *

estado = "apagado"

#Funciones
def cambiar():

    global estado

    if estado == "apagado":
        boton1.place(x=130, y=90)
        boton0.place(x=4000, y=90)
        estado = "encendido"
    else:
        boton0.place(x=130, y=90)
        boton1.place(x=4000, y=90)
        estado="apagado"

window= Tk()
window.title("Etiqueta con imagen")
window.geometry("500x500")

apagada=PhotoImage(file="bulbOff.png")
encendida=PhotoImage(file="bulbOn.png")

boton0= Button(window,image=apagada,command=cambiar)
boton0.place(x=130,y=90)

#Otra imagen

boton1= Button(window, image=encendida,command=cambiar)
boton1.place(x=4000, y=100)

window.mainloop()
