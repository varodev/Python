#Poner un color para "Aumentar" y otro colo para "Disminuir"

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

def aumentar ():
    estilo.configure("black.Horizontal.TProgressbar", background="yellow")
    valor= bar['value']
    valor+=10
    bar['value']=valor
    if bar['value'] >= 100:
       boton['text']="Disminuir" 

def disminuir ():
    estilo.configure("black.Horizontal.TProgressbar", background="blue")
    valor= bar['value']
    valor-=10
    bar['value']=valor
    if bar['value'] <= 0:
       boton['text']="Aumentar" 

def comprobar ():
    if boton['text']=="Aumentar":
        aumentar()
    else:
        disminuir()

ventana=Tk()
ventana.title("Progress Bar")
ventana.geometry("300x250")

estilo= ttk.Style()
estilo.theme_use("default")

bar = Progressbar(ventana, length=200, style="black.Horizontal.TProgressbar")
bar['value']=0

bar.pack(pady=18)

boton=Button(ventana,text="Aumentar", command=comprobar)
boton.pack()


ventana.mainloop()
