from tkinter import *
from tkinter.ttk import *

def enviar():
    valor=combo.get()
    label["text"]=valor



ventana = Tk()
ventana.title("Combobox")

label= Label(ventana, text=" ? ")
label.pack(pady=20)

combo= Combobox(ventana)
combo["values"]=(1,2,3,4,5,"Otra cosa")
combo.current(5) #Posición por defecto empezando por 0
combo.pack()

button1=Button(ventana, text="Enviar", command=enviar)
button1.pack()
