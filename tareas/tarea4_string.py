def main():
    nombre = input("Introduce nombre\n")
    apellido = input("Introduczca apellido \n")
    deporte = input("introduzca su deporte favorito: \n")

    cadena_salida = nombre + "##" + apellido + "&&" + deporte

    print(cadena_salida)

if __name__=="__main__":
    main()