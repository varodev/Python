"""Realiza un programa que pida números al usuario hasta que introduzca 0 o -1. 
Debe mostrar como salida la suma de los números pares por un lado 
y la suma de los impares por otro.
"""

def main():
    suma_num_pares = 0
    suma_num_impares = 0
    numero_usuario = int(input("Intro num:\n"))

    while(numero_usuario != 0) and (numero_usuario != -1):
        if ((numero_usuario % 2) == 0):
            suma_num_pares += numero_usuario
        else:
            suma_num_impares += numero_usuario

        numero_usuario = int(input("Intro num:\n"))
    
    print(f"La suma de los pares es: {suma_num_pares}\n")
    print(f"La suma de los imparesa es: {suma_num_impares}")


if __name__ == "__main__":
    main()