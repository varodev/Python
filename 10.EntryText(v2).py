from tkinter import *

def enviar():
    sunombre=txt1.get()
    suapellido=txt2.get()
    supass=txt3.get()
    print(sunombre + " " + suapellido)
    resultado["text"]= (sunombre + " " + suapellido + " Su pass es " + supass)


ventana= Tk()
ventana.title("Entrada de texto")

formulario=Frame(ventana)
formulario.pack(padx=10,pady=18)

lb1=Label(formulario,
          text="Nombre",
          font=("Times",18))
lb1.grid(column=0,row=0)
txt1=Entry(formulario,
           width=40,
           font=("Times",18))
txt1.grid(column=1,row=0)
lb2=Label(formulario,
          text="Apellidos",
          font=("Times",18))
lb2.grid(column=0,row=1)
txt2=Entry(formulario,
           width=40,
           font=("Times",18))
txt2.grid(column=1,row=1)
lb3=Label(formulario,
          text="Contraseña",
          font=("Times",18))
lb3.grid(column=0,row=2)
txt3=Entry(formulario,
           show="*",  #Para ocultar la contraseña al incluirla
           width=40,
           font=("Times",18))
txt3.grid(column=1,row=2)


botones=Frame(ventana)
botones.pack()
boton1=Button(botones,text="Enviar",font=("Helvetica",15), command=enviar)
boton1.pack(pady=8)
resultado=Label(botones, text=" ")
resultado.pack()
