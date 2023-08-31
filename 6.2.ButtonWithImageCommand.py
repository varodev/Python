from tkinter import *

#Funciones
def imprimir():
    print("Buenas tardes")



window= Tk()
window.title("Etiqueta con imagen")
window.geometry("500x500")

apagada=PhotoImage(file="../images/bulbOff.png")
encendida=PhotoImage(file="../images/bulbOn.png")

etiqueta1= Label(window,image=apagada).place(x=260,y=100)


#Otra imagen

boton1= Button(window, image=encendida,command=imprimir)
boton1.place(x=260, y=100)

window.mainloop()
