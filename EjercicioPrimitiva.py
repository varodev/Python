#Juego de la primitiva.
#El objetivo es conseguir seis números aleatorios ordenados (que no se repitan) del 1 al 49 (incluidos).
#Con un menú, "1" para jugar y "q" para salir.

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
