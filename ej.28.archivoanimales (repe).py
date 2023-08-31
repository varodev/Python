#Ejercicio 8/11/18. Objetivo: Crear un programa que almacene nombre de animales
#en un archivo. Los debe almacenar separados por comas.
#Hacer un menú para insertar los animales y otro para mostrarnos los animales
#(cada uno en una línea, númerados desde el 1 hasta el total de animales que tengamos).
############################################
import os 
############################################
print("1. Insertar alimales \n 2. Mostrar la lista de animales \n")
opcionmenu=input(" 1 o 2 :  ")
print ("")
######################################
archivo=open("Animales.txt","a")
##################################
if opcionmenu=="1":
    print("inserte el nombre del animal")
    print("")
    newanimal=input()
    print("")
    archivo=open("Animales.txt","a")
    archivo.write(newanimal + ",")
    archivo.close()
if opcionmenu=="2":
    print("Mostrarmos toda la lista de animales")
    print("")
    archivo=open("Animales.txt","r")
    #print(archivo.read ())
    archivomod=archivo.read()
    print(archivomod.split(","))
