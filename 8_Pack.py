from tkinter import *

window = Tk()
window.title("Ejemplo pack()")
window.geometry("300x300")
etiqueta= Label(window, text="Mi etiqueta",bg="yellow")
etiqueta2= Label(window, text="Otra etiqueta",bg="yellow")
#etiqueta.grid(column=0, row=0)
#etiqueta.place(x=10, y=10)
#etiqueta.pack(fill=X) #Se rellena horizontalmente
etiqueta.pack(fill=X,pady=10, padx=15)
etiqueta2.pack(fill=X,pady=10,padx=20)

boton1=Button(window,text="Boton1",bg="black",fg="yellow")
boton1.pack(side=TOP, fill=Y)
boton2=Button(window,text="Boton2",bg="red",fg="white")
boton2.pack(side=TOP,fill=Y)

window.mainloop()
