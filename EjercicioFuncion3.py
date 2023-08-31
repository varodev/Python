#Escriba un programa que pida la anchura de un triángulo
#y dibuje una sucesión de triángulos con caracteres producto (*):
#Anchura del triángulo: 3

#   *
#   * *
#   * * *
#   * *
#   *
#   *
#   * *
#   *
#   *


#Pintar Triángulo:

def pintarTriangulo(lado):
    for x in range(t,lado+t):
        print((" "*(lado-x) + "*"*x) - (" "*(lado-x)))

print("Inserte el lado: ")
t=int(input())
pintarTriangulo(t)



