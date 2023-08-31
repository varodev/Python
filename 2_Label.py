from tkinter import *
 
window = Tk()
window.title("Bienvenidos a la primera GUI en Python")
lbl = Label(window, text="Hola")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Hola2")
lbl2.grid(column=1, row=1)
lbl3 = Label(window, text="Hola3")
lbl3.grid(column=2, row=2)



window.mainloop()
