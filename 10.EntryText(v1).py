from tkinter import *

def enviar():
    sunombre=txt1.get()
    suapellido=txt2.get()
    print(sunombre + " " + suapellido)
    resultado["text"]= (sunombre + " " + suapellido)


ventana= Tk()
ventana.title("Entrada de texto")

formulario=Frame(ventana)
formulario.pack(padx=10,pady=18)

lb1=Label(formulario,text="Nombre",font=("Arial",18))
lb1.grid(column=0,row=0)
txt1=Entry(formulario, width=40,font=("Arial",18))
txt1.grid(column=1,row=0)
lb2=Label(formulario,text="Apellidos",font=("Arial",18))
lb2.grid(column=0,row=1)
txt2=Entry(formulario, width=40,font=("Arial",18))
txt2.grid(column=1,row=1)

botones=Frame(ventana)
botones.pack()
boton1=Button(botones,text="Enviar",font=("Helvetica",15), command=enviar)
boton1.pack(pady=8)
resultado=Label(botones, text=" ")
resultado.pack()
