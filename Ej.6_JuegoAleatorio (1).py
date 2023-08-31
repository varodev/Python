import random
from tkinter import *


##### FUNCIONES


numeros=[]

def empezar():
    print("Hola")
    generar()

def generar():
    global numeros
    global introducidos
    introducidos=[]
    while len(numeros)< 9:
        x = random.randrange(1,10)
        if x not in numeros:
            numeros.append(x)
    boton1['text']=numeros[0]
    boton2['text']=numeros[1]
    boton3['text']=numeros[2]
    boton4['text']=numeros[3]
    boton5['text']=numeros[4]
    boton6['text']=numeros[5]
    boton7['text']=numeros[6]
    boton8['text']=numeros[7]
    boton9['text']=numeros[8]

    
    botones= teclado.winfo_children()
    for x in botones:      
        x['state']=NORMAL
        x['fg']= "black"
    etiqueta.place(x=1000,y=1000)
    teclado.after(3000, vaciar)


def vaciar():

    botones= teclado.winfo_children()
    for x in botones:      
        x['fg']= "gray"
      
def comprobar():
    resultado=[1,2,3,4,5,6,7,8,9]
    if introducidos==resultado:
        print("Correcto")
        etiqueta['text']="¡Correcto!"
        etiqueta['bg']="green"
    else:
        print("Fallo")
        etiqueta['text']="¡Fallo!"
        etiqueta['bg']="orange"
    etiqueta.place(x=10,y=10)
    

    
introducidos=[]

def c1():
    numero=boton1['text']
    boton1['text']=""
    boton1['state']=DISABLED
    introducidos.append(numero)
    if len(introducidos)==9:
        comprobar()

def c2():
    numero=boton2['text']
    boton2['text']=""
    boton2['state']=DISABLED
    introducidos.append(numero)
    if len(introducidos)==9:
        comprobar()

def c3():
    numero=boton3['text']
    boton3['text']=""
    boton3['state']=DISABLED
    introducidos.append(numero)
    if len(introducidos)==9:
        comprobar()

def c4():
    numero=boton4['text']
    boton4['text']=""
    boton4['state']=DISABLED
    introducidos.append(numero)
    if len(introducidos)==9:
        comprobar()
    
def c5():
    numero=boton5['text']
    boton5['text']=""
    boton5['state']=DISABLED
    introducidos.append(numero)
    if len(introducidos)==9:
        comprobar()

def c6():
    numero=boton6['text']
    boton6['text']=""
    boton6['state']=DISABLED
    introducidos.append(numero)
    if len(introducidos)==9:
        comprobar()
def c7():
    numero=boton7['text']
    boton7['text']=""
    boton7['state']=DISABLED
    introducidos.append(numero)
    if len(introducidos)==9:
        comprobar()
def c8():
    numero=boton8['text']
    boton8['text']=""
    boton8['state']=DISABLED
    introducidos.append(numero)
    if len(introducidos)==9:
        comprobar()
def c9():
    numero=boton9['text']
    boton9['text']=""
    boton9['state']=DISABLED
    introducidos.append(numero)
    if len(introducidos)==9:
        comprobar()

##### INTERFACE GRÁFICA

ventana=Tk()
ventana.title("Juego Aleatorio")
teclado=Frame(ventana)
teclado.config(bg="gray")
teclado.pack(pady=10,padx=10)
boton1=Button(teclado,
              text="*",
              bg="gray",
              font= ("Times", 22),
              width=4,
              command=c1)
boton1.grid(column=0, row=0)
boton2=Button(teclado,
              text="*",
              bg="gray",
              font= ("Times", 22),
              width=4,
              command=c2)
boton2.grid(column=1, row=0)
boton3=Button(teclado,
              text="*",
              bg="gray",
              font= ("Times", 22),
              width=4,
              command=c3)
boton3.grid(column=2, row=0)
boton4=Button(teclado,
              text="*",
              bg="gray",
              font= ("Times", 22),
              width=4,
              command=c4)
boton4.grid(column=0, row=1)
boton5=Button(teclado,
              text="*",
              bg="gray",
              font= ("Times", 22),
              width=4,
              command=c5)
boton5.grid(column=1, row=1)
boton6=Button(teclado,
              text="*",
              bg="gray",
              font= ("Times", 22),
              width=4,
              command=c6)
boton6.grid(column=2, row=1)
boton7=Button(teclado,
              text="*",
              bg="gray",
              font= ("Times", 22),
              width=4,
              command=c7)
boton7.grid(column=0, row=2)
boton8=Button(teclado,
              text="*",
              bg="gray",
              font= ("Times", 22),
              width=4,
              command=c8)
boton8.grid(column=1, row=2)
boton9=Button(teclado,
              text="*",
              bg="gray",
              font= ("Times", 22),
              width=4,
              command=c9)
boton9.grid(column=2, row=2)

etiqueta=Label(teclado,
               text="Fallo",
               font=("Times",24))

inicio=Frame(ventana)
inicio.pack()
botonInicio=Button(inicio,
                   text="Empezar",
                   font= ("Times", 22), 
                   command=empezar)
botonInicio.pack(pady=15)
