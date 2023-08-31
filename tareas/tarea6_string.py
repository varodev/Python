def main():
    tamanio_palabra_mas_larga = 0
    palabra_entrada = input("Introduzca una palabra: \n")

    while (palabra_entrada != "salir"):
        if (len(palabra_entrada) > tamanio_palabra_mas_larga):
            tamanio_palabra_mas_larga = len(palabra_entrada)

        palabra_entrada =  input("Introduzca una palabra: \n")

    print(f"El tamaño de la palabra más larga es: {tamanio_palabra_mas_larga}")
    
if __name__=="__main__":
    main()