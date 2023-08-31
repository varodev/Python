#Funcion que imprime un rectángulo.

def area(b,h):
    for x in range (h):
        print("*"*b)

def area2(b,h):   # No utilizar el for. Hay que utilizar while.
    i=0
    while i < h:
        print("*"*b)


alto=int(input("Inserte la altura:\n"))
base=int(input("Inserte la base:\n"))

area2(base,alto)



