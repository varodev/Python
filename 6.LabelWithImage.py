from tkinter import *

window= Tk()
window.title("Etiqueta con imagen")
window.geometry("500x500")

imagen1=PhotoImage(file="bulbOff.png")
imagen2=PhotoImage(file="bulbOn.png")

etiqueta1= Label(window,image=imagen2)
etiqueta1.grid(column=0,row=0)



window.mainloop()
