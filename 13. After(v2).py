from tkinter import *

def cambiar():
    valor=etiqueta['text']
    valor+=1
    etiqueta['text']=valor
    if valor < 10:    #Se cambia la etiqueta cada segundo desde 1 hasta 10.
        ventana.after(1000,cambiar)
    
        
ventana = Tk()
ventana.title("After")

etiqueta=Label(ventana,
               text=1,
               font=("Arial",40))


etiqueta.pack(pady=30)
ventana.after(1000,cambiar)

ventana.mainloop()


