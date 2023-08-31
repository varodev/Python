from tkinter import *

def cambiar():
    valor=etiqueta['text']
    valor+=1
    etiqueta['text']=valor
        
ventana = Tk()
ventana.title("After")

etiqueta=Label(ventana,
               text=1,
               font=("Arial",40))


etiqueta.pack(pady=30)
ventana.after(1000,cambiar)

ventana.mainloop()

#Se cambia la etiqueta de 1 a 2
