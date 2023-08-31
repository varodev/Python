def main():
    texto_a_repetir = input("Intro texto \n")
    numero_veces = int(input("Cuántas veces quiere que lo repita? \n"))

    for contador in range(numero_veces):
        print(texto_a_repetir)

if __name__ == "__main__":
    main()


    