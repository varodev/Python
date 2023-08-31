def main():
    FIN = "FIN"
    TAM_BLOQUE = 2
    posicion = 0
    salir = False
    cadena_entrada = input("Intro cadena entrada: \n")

    while ((posicion + TAM_BLOQUE) < len(cadena_entrada)):
        cadena_salida = cadena_entrada[posicion:posicion+2]
        print(cadena_salida)
        posicion+=TAM_BLOQUE

    #Si es un número impar tenemos que mostrar el último caracter
    print(cadena_entrada[posicion:])


if __name__=="__main__":
    main()