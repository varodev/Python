#Escriba un programa con una función que pida la anchura y altura de un rectángulo y el caracter a utilizar en el dibujo:
#Anchura del rectángulo: 5
#Altura del rectángulo: 3
#Carácter a utilizar: o
#o o o o o
#o o o o o
#o o o o o


#Funcion que imprime un rectángulo.

def area(a,b,c):
    for x in range(a):
        print(c*b)
        
#a=alto, b=base, c=caracter

a=int(input("Inserte la altura:\n"))
b=int(input("Inserte la base:\n"))
c=input("Inserte el caracter:\n")

area(a,b,c)
