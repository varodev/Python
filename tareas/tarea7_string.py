def main():
    texto_a_buscar = ""
    texto_nuevo = ""
    nueva_busqueda = "si"
    salir = False
    cadena_entrada = input("Intro cadena de entrada: \n")

    while (nueva_busqueda == "si"):
        texto_a_buscar = input("Intro texto a buscar: \n")
        texto_nuevo = input("Intro nuevo texto: \n")

        cadena_reemplazada = cadena_entrada.replace(texto_a_buscar, texto_nuevo)
        print(cadena_reemplazada)
        cadena_entrada = cadena_reemplazada
        nueva_busqueda = input("Desea usted realizar otra búsqueda y reemplazo? \n")
    


if __name__=="__main__":
    main()