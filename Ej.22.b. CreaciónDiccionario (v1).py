
#Ejercicio diccionario:
#Enunciado: Se nos solicita un número (entero) y guarda en un diccionario
#como clave la cantidad de números insertada, empezando por uno, y como valor la clave multiplicada
#por cinco.

print("Inserte un número entero para el ejercicio")
cantidad=input()
solucion={}
solucionB={}

#Código
a=1
cantidad=int(cantidad)
for x in range(cantidad):
    solucion[a]=a*5
    a=a+1
    
print(solucion)


#Otro codigo

for x in range(cantidad):
   solucionB[x+1]=(x+1)*5

print(solucionB)
