
def main():
    codigo_entrada = input("Intro el código de la serie: \n")
    if (codigo_entrada == "001"):
        print("La serie es La casa de papel, puntuación 9");
    elif (codigo_entrada == "002"):
        print("La serie es Gambito de dama, puntuación 9,8");
    elif (codigo_entrada == "003"):
        print("La serie es El juego del calamar, puntuación 9,4");
    else:
        print("Código erroneo")

if __name__ == "__main__":
    main()