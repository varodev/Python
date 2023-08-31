def main():
    FIN = "FIN"
    tam_bloque = 0
    posicion = 0
    salir = False
    desea_continuar = "SI"

    while (desea_continuar.upper() != FIN):

        cadena_entrada = input("Intro cadena entrada: \n")
        tam_bloque = int(input("Intro tam bloque: \n"))

        while ((posicion + tam_bloque) < len(cadena_entrada)):
            cadena_salida = cadena_entrada[posicion:(posicion+tam_bloque)]
            print(cadena_salida)
            posicion+=tam_bloque
        
        print(cadena_entrada[posicion:])
        posicion = 0
        desea_continuar = input("Desea repetir la operación?")


if __name__=="__main__":
    main()