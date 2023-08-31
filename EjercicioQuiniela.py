#Juego de la quiniela, con los valores 1-x-2 (son valores string, no números enteros). 
#El objetivo es conseguir 15 posiciones, con alguno de estos 3 valores (pueden repetirse).
#Con un menú, "1" para jugar y "q" para salir.


lista=[1,x,2] # posición 0,1,2
valor=random(0-2) # de las posiciones 0,1,2
quiniela.append=lista[valor] # con append se añade un nuevo valor, asi hasta 15 veces.


"""
import random

def generarNumeros():
    lista=[]
    while len(lista)<6:
        y=random.randrange(1,50)
        if y not in lista:
            lista.append(y)
    lista.sort()
    print(lista)

generarNumeros()
"""
