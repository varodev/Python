def main():
    numero1 = int(input("Intro numero 1: "))
    numero2 = int(input("Intro numero 2:"))

    if (numero1 < numero2):
        print("El numero 1 es menor que el numero 2")
    elif (numero1 > numero2):
        print(("El numero 1 es mayor que el numero 2"))
    else:
        print("Los numeros son iguales")

if __name__ == "__main__":
    main()