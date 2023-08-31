def main():
    resultado = 0
    numero1 = int(input("Intro numero 1: "))
    numero2 = int(input("Intro numero 2:"))
    conversion = input("Elija la operación: +,-,*,/ \n")

    if (conversion == "+"):
        resultado = numero1 + numero2
    elif (conversion == "-"):
        resultado = numero1 - numero2
    elif (conversion == "*"):
        resultado = numero1 * numero2
    elif (conversion == "/"):
        resultado = numero1 / numero2
    else:
        print("Opción erronea")

    print(f"El resultado es: {resultado}")

if __name__ == "__main__":
    main()
    