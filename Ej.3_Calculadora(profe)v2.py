from tkinter import *

def op1():
    global operacion
    if operacion=="0":
        operacion="1"
    else:
        operacion=operacion+"1"
    etiqueta["text"]=operacion
def op2():
    global operacion
    if operacion=="0":
        operacion="2"
    else:
        operacion=operacion+"2"
    etiqueta["text"]=operacion
def op3():
    global operacion
    if operacion=="0":
        operacion="3"
    else:
        operacion=operacion+"3"
    etiqueta["text"]=operacion
def op4():
    global operacion
    if operacion=="0":
        operacion="4"
    else:
        operacion=operacion+"4"
    etiqueta["text"]=operacion
def op5():
    global operacion
    if operacion=="0":
        operacion="5"
    else:
        operacion=operacion+"5"
    etiqueta["text"]=operacion
def op6():
    global operacion
    if operacion=="0":
        operacion="6"
    else:
        operacion=operacion+"6"
    etiqueta["text"]=operacion
def op7():
    global operacion
    if operacion=="0":
        operacion="7"
    else:
        operacion=operacion+"7"
    etiqueta["text"]=operacion
def op8():
    global operacion
    if operacion=="0":
        operacion="8"
    else:
        operacion=operacion+"8"
    etiqueta["text"]=operacion
def op9():
    global operacion
    if operacion=="0":
        operacion="9"
    else:
        operacion=operacion+"9"
    etiqueta["text"]=operacion
def op0():
    global operacion
    if operacion=="0":
        operacion="0"
    else:
        operacion=operacion+"0"
    etiqueta["text"]=operacion
def opPunto():
    global operacion
    if operacion=="0":
        operacion="0."
    else:
        operacion=operacion+"."
    etiqueta["text"]=operacion
def opMas():
    global operacion
    if operacion=="0":
        operacion="0+"
    else:
        operacion=operacion+"+"
    etiqueta["text"]=operacion
def opMenos():
    global operacion
    if operacion=="0":
        operacion="0-"
    else:
        operacion=operacion+"-"
    etiqueta["text"]=operacion
def opPor():
    global operacion
    if operacion=="0":
        operacion="0*"
    else:
        operacion=operacion+"*"
    etiqueta["text"]=operacion    
def opDividir():
    global operacion
    if operacion=="0":
        operacion="0/"
    else:
        operacion=operacion+"/"
    etiqueta["text"]=operacion
def opC():
    global operacion
    operacion="0"
    etiqueta["text"]=operacion
def opIgual():
    global operacion
    operacion=str(eval(operacion))
    etiqueta["text"]=operacion
    
ventana=Tk()
ventana.title("Ejercicio 3. Calculadora")
#ventana.geometry("300x300")
"""
imagen= PhotoImage(file="calculadora.png")
imagen2= PhotoImage(file="vacio.png")
fondo=Label(ventana,image=imagen).place(x=0,y=0)
"""

operacion="0"


pantalla=Frame(ventana)
pantalla.pack(fill=X)
etiqueta=Label(pantalla,text=operacion,bg="yellow",font=("Times",18),anchor=E)
etiqueta.pack(fill=X,pady=15)



teclado=Frame(ventana)
teclado.pack(fill=X)

boton1=Button(teclado,text="1", width=5,command=op1).grid(column=0,row=1)
boton2=Button(teclado,text="2", width=5,command=op2).grid(column=1,row=1)
boton3=Button(teclado,text="3", width=5,command=op3).grid(column=2,row=1)
botonMas=Button(teclado,text="+", width=5,command=opMas).grid(column=3,row=1)
boton4=Button(teclado,text="4", width=5,command=op4).grid(column=0,row=2)
boton5=Button(teclado,text="5", width=5,command=op5).grid(column=1,row=2)
boton6=Button(teclado,text="6", width=5,command=op6).grid(column=2,row=2)
botonMenos=Button(teclado,text="-", width=5,command=opMenos).grid(column=3,row=2)
boton7=Button(teclado,text="7", width=5,command=op7).grid(column=0,row=3)
boton8=Button(teclado,text="8", width=5,command=op8).grid(column=1,row=3)
boton9=Button(teclado,text="9", width=5,command=op9).grid(column=2,row=3)
botonPor=Button(teclado,text="*", width=5,command=opPor).grid(column=3,row=3)
botonC=Button(teclado,text="C", width=5,command=opC).grid(column=0,row=4)
boton0=Button(teclado,text="0", width=5,command=op0).grid(column=1,row=4)
botonPunto=Button(teclado,text=".", width=5,command=opPunto).grid(column=2,row=4)
botonDividir=Button(teclado,text="/", width=5,command=opDividir).grid(column=3,row=4)

igual=Frame(ventana)
igual.pack()

botonIgual=Button(igual,text="=", width=10,command=opIgual)
botonIgual.pack(pady=6)


ventana.mainloop()
