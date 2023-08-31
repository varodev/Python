"""Realiza un programa que tenga declarado internamente un número. 
Se le pedirá al usuario que introduzca números hasta que acierte. 
Cada vez que introduzca un número se le indicará si es mayor o menor 
que el número almacenado internamente o si ha acertado"""

def main():
    NUMERO_SECRETO = 7
    numero_usuario = 0
    acertado = False

    while (numero_usuario != NUMERO_SECRETO):
        numero_usuario = int(input(("Intro número\n")))
        if(numero_usuario > NUMERO_SECRETO):
            print(("El número introducido es mayor\n"))
        elif(numero_usuario < NUMERO_SECRETO):
            print("El número introducido es menor\n")

    print(("Enhorabuena!!"))

if __name__ == "__main__":
    main()