def main():
    texto_entrada = input("Introduce un texto\n")
    subcadena_a_cambiar = input("Intro cadena a sustituir\n")
    nueva_subcadena = input("Intro nueva subcadena \n")

    nuevo_texto = texto_entrada.replace(subcadena_a_cambiar, nueva_subcadena)
    print(texto_entrada)
    print(nuevo_texto)

if __name__=="__main__":
    main()