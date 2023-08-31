from tkinter import *
import tkinter 
window = Tk()
window.title("Ejercicio 1 Etiquetas")
etiquetas=[]
contador=0
for c in range (4):
    for f in range (5):
        etiquetas.append(Label(window, text="       --Columna "+str(c)+". Fila " + str(f)+"--      "))
        etiquetas[contador].grid(column=c, row=f)
        contador+=1
                

window.mainloop()
