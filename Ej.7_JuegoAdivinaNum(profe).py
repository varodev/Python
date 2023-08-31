"""El objetivo es hacer un programa (juego) que nos genere
un número aleatorio entre el 1 y el 100.
El objetivo es adivinarlo, diciéndonos si el número introducido
es menor o mayor al número.
Al final nos dirá a cuántos intentos lo hemos adividado."""

import random
#from tkinter.ttk import *
from tkinter import *

contador=0

def generarAleatorio():
    global numero
    numero=random.randrange(1,101)
    print(numero)
    return numero

def iniciar():
    global contador
    global numero
    contador=0
    numero=generarAleatorio()
    entrada.delete(0,END)
    resultado["text"]=""

def limpiaEntry():
    entrada.delete(0,END)

def comprobar():
    global contador
    global numero
    print(contador)
    insertado=int(entrada.get())
    if numero == insertado:
        contador+=1
        texto=("Correcto. Lo has conseguido al \n" + str(contador)+ " intento/s.")
        resultado["text"]=texto
    else:
        contador+=1
        if insertado < numero:
            texto=("Fallo. El número insertado("+str(insertado)+") es \n menor al número a adivinar")
            resultado["text"]=texto
        else:
            texto=("Fallo. El número insertado ("+str(insertado)+") es \n mayor al número a adivinar")
            resultado["text"]=texto
    #entrada.delete(0,END)
    ventana.after(2000,limpiaEntry)
   
ventana= Tk()
ventana.title("Juego Simulacro")
ventana.geometry("300x300")
boton1=Button(ventana,text="Iniciar juego",font=("Times",18),command=iniciar)
boton1.pack(pady=25)
entrada=Entry(ventana,width=5,font=("Times",18))
entrada.pack(pady=10)
boton2=Button(ventana,text="Comprobar",font=("Times",18),command=comprobar)
boton2.pack(pady=15)
resultado=Label(ventana,text="",font=("Arial",13))
resultado.pack(pady=10)
ventana.mainloop()


iniciar()

