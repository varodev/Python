#Ejercicio concatenar lista
#Familia Lopez Gonzalez
#Concatenar los apellidos a cada uno de los miembros de la lista.

lista=["Jose Antonio", "Luis", "Felipe", "Antonio", "Jose", "Ana", "Maria"]

apellidos=" Lopez Gonzalez"

contador=0

for x in lista:
    lista[contador]=x+apellidos
    contador+=1
print(lista)
