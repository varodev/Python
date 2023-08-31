from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

def aumentar ():
    valor= bar['value']
    valor+=10
    bar['value']=valor
    if bar['value'] >= 100:
       boton['text']="Disminuir" 

def disminuir ():
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
estilo.configure("black.Horizontal.TProgressbar", background="yellow")

bar = Progressbar(ventana, length=200, style="black.Horizontal.TProgressbar")
bar['value']=0

bar.pack(pady=18)

boton=Button(ventana,text="Aumentar", command=comprobar)
boton.pack()


ventana.mainloop()
