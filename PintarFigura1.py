#Pintar cuadrado

def pintarFigura(n):
    for x in range(n):
        print("*"*n)

print("Inserte la dimensión del cuadrado a pintar:")
x=int(input())
pintarFigura(x)
