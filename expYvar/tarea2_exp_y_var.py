def main():
    PI=3.14
    radio = 0
    superficie_circulo = 0

    radio = int(input("Introduzca el radio del círculo: "))

    superficie_circulo = PI*(radio**2)

    print(f"La superficie del círculo es {superficie_circulo}")

if __name__ == "__main__":
    main()