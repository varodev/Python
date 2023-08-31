#Ejercicio 8/11/18. Objetivo: Crear un programa que almacene nombre de animales
#en un archivo. Los debe almacenar separados por comas.
#Hacer un menú para insertar los animales y otro para mostrarnos los animales
#(cada uno en una línea, númerados desde el 1 hasta el total de animales que tengamos).


# Para crear un archivo nuevo se utiliza “w”:
# archivo=open("ej.28.archivoanimales.csv", "a")

archivo=open("ej.28.archivoanimales.csv", "a")
animales=[]

especie=input("Escribe la especie de animal:\n")
    #Por ejemplo: gato, vaca, ratón..
grupo=input("¿A qué grupo animal pertenece?:\n")
    #Clasificados en veretebrados o invertebrados
tipo=input("Escribe el tipo de animal:\n")
    #Vertebrados: mamíferos, pájaros, peces, reptiles, anfibios.
    #Invertebrados:ctenóforos, cnidarios, equinodermos y artrópodos

animales.append(especie+",")
animales.append(grupo+",")
animales.append(tipo)

for x in animales:
    archivo.write(x)
archivo.write(";")
archivo.close()

def insertar():
    especie=input("Escribe otra especie de animal:\n")
    grupo=input("¿A qué grupo animal pertenece?:\n")
    tipo=input("Escribe el tipo de animal:\n")
    archivo=open("ej.28.archivoanimales.csv", "a")
    archivo.write("FIN DE LISTADO:\n")
    archivo.close()
    main()

def ver():
    archivo=open("ej.28.archivoanimales.csv", "r")
    print(archivo.read())
    archivo.close()
    main()

def salir():
    print("Saliendo")

def main():
    print("A para añadir un animal a la lista:\n""V para ver la lista creada:\n")
    opcion=input("Elige una opción:\n")
    
    if opcion=="A":
        insertar()
    if opcion=="V":
        ver()
    if opcion=="S":
        salir()
main()
