# Escribe un programa Python que tenga una lista interna de números, obtenga un número aleatorio 
# de esa lista (elemento = random.choice(lista)) y le pedirá al usuario que lo acierte en un máximo 
# de 4 intentos. Cada vez que el usuario cometa un error se le indicará si el número es mayor o menor. 
# Cuando haya acertado o bien finalizado el número de intentos se volverá a escoger un número de la 
# lista al azar y se repetirá el proceso. Así indefinidamente hasta que el usuario indique 
# que quiere finalizar.
import random

def main():
    lista_numeros = [2,5,77,99,345,2,44,75,93,55,33,22]
    MAX_INTENTOS = 3
    continuar = "si"

    while(continuar == "si"):
        numIntento = 0
        acertado = False
        numero_secreto = random.choice(lista_numeros)
        print(lista_numeros)
        comprobar_numero_secreto(numero_secreto,MAX_INTENTOS)
        print(f"El numero secreto es {numero_secreto}")

        continuar = input("Desea continuar?")

def comprobar_numero_secreto(numero_secreto, max_intentos):
    numero_intentos = 0
    numero_usuario = 0
    acertado = False

    while ( (numero_intentos < max_intentos) and ( not acertado) ):
        numero_usuario = int(input("A ver si aciertas el número secreto!: \n"))
        if (numero_usuario == numero_secreto):
            acertado = True
            print("Enhorabuena! has acertado!")
        elif (numero_usuario > numero_secreto):
            print(" El número secreto es menor")
        else:
            print(" El número secreto es mayor")
        
        numero_intentos += 1

    if (numero_intentos == max_intentos):
        print("Has llegado al número máximo de intentos")

if __name__ == "__main__":
    main()