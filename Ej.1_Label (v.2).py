from tkinter import *
 
window = Tk()
window.title("Ejercicio 1: ETIQUETAS")


etiqueta=["Et1", "Et2", "Et3", "Et4", "Et5", "Et6", "Et7", "Et8", "Et9", "Et10", "Et11", "Et12", "Et13", "Et14", "Et15", "Et16", "Et17", "Et18", "Et19", "Et20"]

# c = columnas (son 4 columnas)
# f = filas (son 5 filas)

for c in range(4):
    for f in range(5):
        etiqueta[c]=Label(window, text=" columna "+str(c)+", fila "+str(f)+" | ")
        etiqueta[c].grid(column=c, row=f)

window.mainloop()


"""etiqueta=[Label(window, text="col.0,fila.0")
etiqueta[0].grid(column=0, row=0)
"""

"""
lbl = Label(window, text="Hola")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Hola2")
lbl2.grid(column=1, row=1)
lbl3 = Label(window, text="Hola3")
lbl3.grid(column=2, row=2)
"""



