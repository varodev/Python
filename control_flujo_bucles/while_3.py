def main():
    suma_numeros = 0
    salir = False
    numero_entrada = int(input("Intro número \n"))
    
    while not (salir):
        suma_numeros += numero_entrada
        numero_entrada = int(input("Intro número"))

        if (numero_entrada == 1) or (numero_entrada > 10):
            salir = True

    print(suma_numeros)

if __name__ == "__main__":
    main()

    