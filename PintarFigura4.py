#Pintar cuadrado
"""
def pintarFigura(n):
    for x in range(n):
        print("*"*n)

print("Inserte la dimensión del cuadrado a pintar:")
x=int(input())
pintarFigura(x)

#Pintar rectángulo

def pintarRectangulo(base, altura):
    for x in range(altura):
        print("*"*base)

print("Inserte la base: ")
b=int(input())
print("Inserte la altura: ")
a=int(input())
pintarRectangulo(b,a)

#Pintar Triángulo Rectángulo 1

def pintarTriangulo1(lado):
    for x in range (1,lado+1):
        print("*"*x)

print("Inserte el lado: ")
l=int(input())
pintarTriangulo1(l)

#Pintar Triángulo Rectángulo 2
def pintarTriangulo2(lado):
    for x in range(1,lado+1):
        print(" "*(lado-x) + "*"*x)

print("Inserte el lado: ")
la=int(input())
pintarTriangulo2(la)
"""
#Pintar Triángulo Rectángulo 3
def pintarTriangulo3(lado):
    for x in range(lado):
        print("*"*(lado-x)+" "*x)

print("Inserte el lado: ")
la=int(input())
pintarTriangulo3(la)
"""
#Pintar Triángulo Rectángulo 4
def pintarTriangulo4(lado):
    for x in range(lado):
        print(" "*x+"*"*(lado-x))

print("Inserte el lado: ")
la=int(input())
pintarTriangulo4(la)

"""
#Pintar Albol Navidad Altura n
#
#Por ejemplo, árbol de alto 3
#
#     *
#    ***
#   *****
#    |||
#
#Por ejemplo, árbol de alto 4
#
#      *
#     ***
#    *****
#   *******
#     |||
#



#Pintar cruz de orden n

#Por ejemplo. Orden 3
#
#      ***
#      ***
#      ***
#   ***===***
#   ***===***
#   ***===***
#      ***
#      ***
#      ***


