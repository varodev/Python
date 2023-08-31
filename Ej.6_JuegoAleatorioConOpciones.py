
### ESTÁ INCOMPLETO ###

from tkinter.ttk import *
from tkinter import *
import random

def jugar():
    nBotones=int(combo.get())
    nSegundos=int(combo2.get())
    crearVentana(nBotones)

def c0():
    print(1)
def c1():
    print(2)
def c2():
    print(3)
def c3():
    print(4)
def c4():
    print(1)
def c5():
    print(2)
def c6():
    print(3)
def c7():
    print(1)
def c8():
    print(2)
def c9():
    print(3)
def c10():
    print(4)
def c11():
    print(4)
def c12():
    print(3)
def c13():
    print(4)
def c14():
    print(4)
comando=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14]

def crearVentana(numero):
    ventana=Tk()
    ventana.title("Ventana de juego")
    teclado=Frame(ventana)
    teclado.pack(pady=10,padx=30)
    global botones
    botones=[]
    fila=0
    columna=0
    for x in range(numero):
        if x%3==0:
            fila+=1
        if columna%3==0:
            columna=0
        botones.append(Button(teclado,
                              text="",
                              bg="gray",
                              width=5,
                              font=("Arial",17),
                              command=comando[x]))
        #botones[x]["bg"]="orange"
        botones[x].grid(column=columna,row=fila)
        columna+=1  

    for x in botones:
        x ["text"]="Manolo"
        x ["bg"]="Orange"

    # Colocar números aleatorios
    numBotones=[]
    maximo=numero+1
    while len(numBotones)< numero:
        x = random.randrange(1,maximo)
        if x not in numBotones:
            numBotones.append(x)

    for x in range(numero):
        botones[x]["text"]=numBotones[x]

        
        
##### Ventana principal
ventanaPrincipal = Tk()
ventanaPrincipal.title("Juego")

label= Label(ventanaPrincipal, text="Cantidad de números")
label.pack(pady=10,padx=20)

combo= Combobox(ventanaPrincipal,font=("Arial", 22),width=2)
combo["values"]=(6,7,8,9,10,11,12,13,14,15)
combo.current(5) #Posición por defecto empezando por 0
combo.pack(padx=7)

label2= Label(ventanaPrincipal, text="Tiempo")
label2.pack(pady=10)
combo2= Combobox(ventanaPrincipal,font=("Arial", 22),width=2)
combo2["values"]=(6,7,8,9,10,11,12,13,14,15)
combo2.current(5) #Posición por defecto empezando por 0
combo2.pack(padx=7)

button1=Button(ventanaPrincipal,text="Jugar",font=("Times",18),command=jugar)
button1.pack(pady=13)
