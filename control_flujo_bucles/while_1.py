def main():
    suma_numeros = 0
    numero_entrada = int(input("Intro número"))

    while (numero_entrada != 0):
        suma_numeros += numero_entrada
        numero_entrada = int(input("Intro número"))

    print(suma_numeros)

if __name__ == "__main__":
    main()

    