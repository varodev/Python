#Ejercicio 24
#Escribe un programa que pida la anchuta de un triangulo y dibuje una sucesion de
#Triengulos con caracteres producto (*)
#Ejemplo anchura de triangulo 3:
#       *
#       **
#       ***
#       **
#       *
#       *
#       **
#       *
#       *
    
def pintarTriangulo(c):
        i=0
        while i < c:
                for x in range (1,(c+1)):
                        print("*"*x)
                for x in range (1,c):
                        print("*"*(c-x))
                c=c-1
c= int(input("Inserte el ancho del triangulo: "))

pintarTriangulo(c)
