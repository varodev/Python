from tkinter import *
from tkinter import messagebox

def click():
        messagebox.showinfo('Información general', 'Mensaje informativo')
        messagebox.showwarning('AVISO', 'Mensaje de aviso')
        messagebox.showerror('ERROR IMPORTANTE', 'Por favor, inserte '+
                             'correctamente todos los campos')


ventana=Tk()
ventana.title("Caja de mensajes")

boton=Button(ventana,text="Hazme click",command=click)
boton.pack(pady=20,padx=20)
