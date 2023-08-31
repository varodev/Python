#Hacer un programa que sea un juego de preguntas y respuestas sobre las Capitales del mundo.
#Al inicio tenemos que insertar un nombre de usuario.
#Tienes que mostrarnos de forma aleatoria 10 preguntas de 20 posibles almacenadas.
#El programa tiene que ser indiferente a insertarlo en mayúsculas o minúsculas.
#Al final nos tiene que mostrar la cantidad de respuestas correctas.
#Al final del juego nos tiene que guardar en un archivo, el nombre del usuario, la fecha
#y hora que ha jugado y la puntuación obtenida, también las respuestas erróneas cometidas.

import random
import datetime 
pais=["grecia","países bajos","austria","hungría","alemania","república checa","reino unido","francia","italia","españa","belgica","dinamarca","finlandia","irlanda","luxemburgo","noruega","rumania","egipto","libia","túnez"]
capital=["atenas","ámsterdam","viena","budapest","berlín","praga","londres","parís","roma","madrid","bruselas","copenague","helsinki","dublin","luxemburgo","oslo","bucarest","el cairo","trípoli","túnez"]
lista=[]

def generarNumeros():
    global lista
    while len(lista)<10:
        y=random.randrange(0,20)
        if y not in lista:
            lista.append(y)

generarNumeros()
print("###############################")
print("#####ADIVINA LAS CAPITALES#####")
print("###############################\n")

nombre= input("Inserta tu nombre: ")

contadorCorrectas=0
contadorIncorrectas=0
error=[]              #Almacena el numero del array del pais y capital que ha fallado el usuario


for x in range (10):
    print("¿Cual es la capital de " +str(pais[lista[x]] +"?"))
    respuesta= input("La capital es: ")
    respuesta=respuesta.lower()
    if respuesta== capital[lista[x]]:
        print("Correcto")
        contadorCorrectas=contadorCorrectas+1
    else:
        print("Incorrecto")
        contadorIncorrectas=contadorIncorrectas+1
        error.append(lista[x])
fecha=datetime.datetime.now()

#Creacion del fichero  
file=open("puntuacion.txt","w")
file.write("NOMBRE DE USUARIO: ")
file.write(nombre)
file.write("\n")
file.write("FECHA DE LA PARTIDA: ")
file.write(str(fecha.day)+"-" +str(fecha.month) +"-" +str(fecha.year))
file.write("\n")
file.write("\n")
file.write("Numero de aciertos: ")
file.write(str(contadorCorrectas))
file.write("\n")
file.write("Numero de fallos: ")
file.write(str(contadorIncorrectas))
file.write("\n")
file.write("\n")
file.write("\n")
file.write("LAS QUE HAS FALLADO: ")
file.write("\n")
for x in error:
    file.write("La capital de " +pais[x] +" es: " +capital[x])
    file.write("\n")
file.close()

#Mostrar los datos por pantalla
print("NOMBRE DE USUARIO: ")
print(nombre)
print("\n")
print("FECHA DE LA PARTIDA: ")
print (str(fecha.day)+"-" +str(fecha.month) +"-" +str(fecha.year))
print("\n")
print("Numero de aciertos: ")
print(str(contadorCorrectas))
print("\n")
print("Numero de fallos: ")
print(str(contadorIncorrectas))
print("\n")
print("LAS QUE HAS FALLADO: ")
print("\n")
for x in error:
    print("La capital de " +pais[x] +" es: " +capital[x])
    print("\n")


