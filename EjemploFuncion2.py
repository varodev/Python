#Funcion que imprime un rectángulo.

def area(b,h):
    for x in range (h):
        print("*"*b)


alto=input("Inserte la altura:\n")
base=int(input("Inserte la base:\n"))

area(base,alto)
