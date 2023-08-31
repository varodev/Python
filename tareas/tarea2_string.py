def main():
    texto_entrada = input("Introduce un texto\n")
    posicion = int(input("Introduczca posición, comenzando en 0 \n"))

    caracter = texto_entrada[posicion]
    print(f"El caracter en la posión {posicion} es {caracter}")

if __name__=="__main__":
    main()