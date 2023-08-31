def main():
    suma_numeros = 0
    numero_entrada = int(input("Intro número \n"))

    while (numero_entrada != 1) and (numero_entrada < 10):
        suma_numeros += numero_entrada
        numero_entrada = int(input("Intro número"))

    print(suma_numeros)

if __name__ == "__main__":
    main()

    