from tkinter import *

window= Tk()
window.title("Etiqueta con imagen")
window.geometry("500x500")

imagen1=PhotoImage(file="images/bulbOff.png")
imagen2=PhotoImage(file="bulbOn.png")

etiqueta1= Label(window,image=imagen2)
#etiqueta1.grid(column=0, row=0)

#Otra imagen

etiqueta2= Label(window, image=imagen2)
etiqueta2.place(x=260, y=100)
window.mainloop()
